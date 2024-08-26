from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from cart.models import Cart
from photos.models import Price
from cart.views import CartView

class OrderView(APIView):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        total = CartView.get_total(self, request)
        context = {
            'cart': cart,
            'total': total,
        }
        return render(request, 'order_list.html', context)
    
    def post(self, request, *args, **kwargs):
        pass
    
orderview = OrderView.as_view()