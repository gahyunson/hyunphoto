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

# class UserSigninview(APIView):
    
#     def get(self, request):
#         return render(request, 'home.html')



from django.shortcuts import redirect
from django.urls import reverse
import google_auth_oauthlib.flow

class UserSigninview(APIView):

    def get(self, request):
        # Create the flow using the client secrets file
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            '../secrets.json',
            scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email']
        )
        flow.redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback'

        # Generate the authorization URL
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes=True,  # Reuse previously granted permissions
            prompt='none'  # Do not prompt for consent if the user is already authenticated
        )

        # Store the state in the session for later validation
        request.session['state'] = state

        # Redirect the user to the Google OAuth2 authorization URL
        return redirect(authorization_url)

# Example of a callback view to handle the redirect back from Google
class GoogleCallbackView(APIView):

    def get(self, request):
        state = request.session['state']

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            '../secrets.json',
            scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'],
            state=state
        )
        flow.redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback'

        # Use the authorization response to fetch the tokens
        authorization_response = request.build_absolute_uri()
        flow.fetch_token(authorization_response=authorization_response)

        # Get the user's credentials
        credentials = flow.credentials

        # Use credentials to interact with Google APIs or store them in your database

        return render(request, 'home.html', {'message': 'Signed in successfully!'})
usersigninview = UserSigninview.as_view()
googlecallbackview = GoogleCallbackView.as_view()

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

