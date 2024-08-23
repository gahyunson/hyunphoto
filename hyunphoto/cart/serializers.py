from rest_framework import serializers
from .models import Cart
from users.models import User
from photos.models import Photo, Price
from photos.serializers import PhotoSerializer, PriceSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = ['user', 'photo', 'price', 'quantity']

    def create(self, validated_data):
        user = validated_data['user']
        photo = validated_data['photo']
        price = validated_data['price']
        quantity = validated_data['quantity']

        return Cart.objects.create(user=user, photo=photo, price=price, quantity=quantity)