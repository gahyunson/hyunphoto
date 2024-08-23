from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status
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
    
    def post(self, request, *args, **kwargs):
        action_type = request.POST.get('action_type')
        cart_item_id = request.POST.get('cart_item')

        if action_type == 'delete':
            cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
            cart_item.delete()
            return redirect('cart')
        
        # elif action_type == 'modify':
        #     new_quantity = request.POST.get('quantity', 1)
        #     Cart.objects.filter(id=cart_item_id, user=request.user).update(quantity=new_quantity)
        #     return redirect('cart')
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
cartview = CartView.as_view()