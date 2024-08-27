from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from cart.models import Cart
from photos.models import Price
from cart.views import CartView
import json 
import secrets
import paypalrestsdk
import os


secrets_file_path = os.path.join('../secrets.json')

# Load the secrets from the JSON file
with open(secrets_file_path, 'r') as f:
    secrets = json.load(f)

paypalrestsdk.configure({
    "mode": "sandbox", 
    "client_id": secrets['PAYPAL_CLIENT_ID'], # Updated
    "client_secret": secrets['PAYPAL_SECRET'], # Updated
})

def create_payment(request):
    cart = Cart.objects.filter(user=request.user)
    total = CartView.get_total(cart)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
        "transactions": [
            {
                "amount": {
                    "total": total['total_price'],  # Total amount in USD
                    "currency": "USD",
                },
                "description": "Payment for Product/Service",
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'payment_failed.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment_success.html')
    else:
        return render(request, 'payment_failed.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')


class OrderView(APIView):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        total = CartView.get_total(cart)
        context = {
            'cart': cart,
            'total': total,
        }
        return render(request, 'order_list.html', context)
    
    
orderview = OrderView.as_view()