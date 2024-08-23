from rest_framework import serializers
from .models import Photo, Price

class PriceSerializer(serializers.Serializer):
    class Meta:
        model = Price 
        fields = '__all__'

class PhotoSerializer(serializers.Serializer):
    price_set = PriceSerializer()
    
    class Meta:
        model = Photo 
        fields = '__all__'
