from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from allauth.socialaccount.models import SocialAccount
from .models import Photo, Price

def home(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, 'photos.html', context)

class PhotoDetailView(APIView):
    permission_classes = [AllowAny]

    def get_price(self, photo_id):
        try:
            return Price.objects.get(photo_id=photo_id)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        photo_id = self.kwargs['photo_id']
        photo = Photo.objects.get(id=photo_id)
        price = photo.price_set.all()
        context = {
            'photo': photo,
            'price': price
        }
        return render(request, 'photo_detail.html', context)
    
    def post(self, request, *args, **kwargs):
        photo_id = self.kwargs['photo_id']
        photo = Photo.objects.get(id=photo_id)
        price = photo.price_set.all()
        print(photo_id, photo, price)


photodetailview = PhotoDetailView.as_view()