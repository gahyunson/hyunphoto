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
import google.oauth2.credentials
import google_auth_oauthlib.flow

class UserSigninview(APIView):
    
    def get(self, request):
        print('session:', request.session.state)
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            '../secrets.json',
            scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email']
            )
        flow.redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback'

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes=True,  # 이미 승인된 권한은 재사용
            prompt='none'  # 사용자가 이미 인증된 경우 권한 승인 화면을 생략
        )
        request.session['state'] = state 

        # return render(request, 'home.html')
        return redirect(authorization_url)

usersigninview = UserSigninview.as_view()

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        logout(request)
        return redirect('/')
    
userlogoutview = UserLogoutView.as_view()

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()

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

