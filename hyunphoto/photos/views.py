from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from allauth.socialaccount.models import SocialAccount
from .models import Photo, Price
from cart.models import Cart
from .serializers import PhotoSerializer, PriceSerializer
from cart.serializers import CartSerializer
from django.db.models import F

def home(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, 'photos.html', context)

class PhotoDetailView(APIView):

    def get(self, request, *args, **kwargs):
        self.methods=('get',)
        self.permission_classes = (AllowAny,)
        photo_id = self.kwargs['photo_id']
        photo = Photo.objects.get(id=photo_id)
        price = photo.price_set.all()

        context = {
            'photo': photo,
            'price': price
        }
        return render(request, 'photo_detail.html', context)
    
    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        '''
        post method -> add to cart
        if already in cart -> increase quantity
        else -> create cart
        '''

        user = request.user.id
        photo_id = request.data['photo_id']
        price_id = request.data['price_id']
        quantity = request.data['quantity']
        print(photo_id, price_id, quantity)

        cart = Cart.objects.filter(user=user, photo_id=photo_id, price_id=price_id)
        print(cart.__dict__)
        if cart:
            cart.update(quantity=F('quantity')+1)
            return render(request, 'cart.html')
        else:
            context = {
                'user': user,
                'photo': photo_id,
                'price': price_id,
                'quantity': quantity
            }

            serializer = CartSerializer(data=context)
            if serializer.is_valid():
                serializer.save()
                return redirect('cart')
        return Response({'message': 'Login required'}, status=status.HTTP_400_BAD_REQUEST)
        


photodetailview = PhotoDetailView.as_view()