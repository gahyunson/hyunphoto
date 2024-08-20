from django.shortcuts import render, redirect
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions 
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from allauth.socialaccount.models import SocialAccount



def home(request):
    # user = request.user
    user = {'user': request.user}
    # context = {
    #     'email': user.email,
    #     'username': user.username,
    #     'password': user.password,
    # }
    # print(context)
    return render(request, 'home.html', user)

def logout_view(request):
    logout(request)
    return redirect('/')

class UserProfileAPI(APIView):
    permission_classes = [AllowAny]
    # authentication_classes = []

    def get(self, request):
        social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
        # print(social_account.__dict__)

        if social_account:
            user_info = {
                'email': request.user.email,
                'username': request.user.username,
                'address': request.user.address,
                'address2': request.user.address2,
                'city': request.user.city,
                'company': request.user.company,
                'nation': request.user.nation,
                'phone': request.user.phone,
                'postal': request.user.postal,
            }
        else:
            user_info = {
                'message': 'not found'
            }
        return render(request, 'profile.html', {'user_info': user_info})
    
    def put(self, request):
        user = request.user 
        # print(user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

