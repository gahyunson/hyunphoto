from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Cart
from photos.models import Price

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get_total(self, request):
        cart = Cart.objects.filter(user=request.user)

        total_price = 0
        total_quantity = 0
        for c in cart:
            price = Price.objects.get(id=c.price.id)
            total_quantity += c.quantity
            total_price += (price.price * c.quantity) 
        total = {
            'total_price': total_price,
            'total_quantity': total_quantity
        }
        return total


    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user)

        total = self.get_total(self.request)
        context = {
            'user': request.user,
            'cart': cart,
            'total': total,
        }
        return render(request, 'cart.html', context)
    
cartview = CartView.as_view()