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
        return Cart.objects.create(**validated_data)