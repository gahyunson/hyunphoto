from django.shortcuts import render, redirect
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions 
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from allauth.socialaccount.models import SocialAccount
from rest_framework import status

class UserSigninview(APIView):
    def get(self, request):
        return render(request, 'home.html')

usersigninview = UserSigninview.as_view()

class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')
    
userlogoutview = UserLogoutView.as_view()

class UserProfileView(APIView):
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
                'postal': request.user.postal,
                'city': request.user.city,
                'nation': request.user.nation,
                'company': request.user.company,
                'phone': request.user.phone,
            }
        else:
            user_info = {
                'message': 'not found'
            }
        return render(request, 'profile.html', {'user_info': user_info})
    
    def put(self, request):
        user = request.user 
        print(user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        user = request.user
        try: 
            user.delete()
            return redirect('/')
        except SocialAccount.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

userprofileview = UserProfileView.as_view()

