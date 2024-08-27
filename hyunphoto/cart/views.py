from django.http import JsonResponse
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

    def put(self, request, *args, **kwargs):
        cart_item_id = request.data.get('cart_item')
        new_quantity = request.data.get('quantity')
        print('cart_item_id:', cart_item_id, 'new_quantity:', new_quantity)
        if not cart_item_id or not new_quantity:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        Cart.objects.filter(id=cart_item_id).update(quantity = new_quantity)
        return JsonResponse({'satus': 'success'}, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        cart_item_id = request.data.get('cart_item')
        print('delete', cart_item_id)
        if not cart_item_id:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        # cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
        cart_item = Cart.objects.filter(user=request.user, id=cart_item_id)
        if cart_item:
            cart_item.delete()
            return JsonResponse({'satus': 'success'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
cartview = CartView.as_view()