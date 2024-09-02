from django.urls import path
from . import views 

urlpatterns = [
    path('google/login/', views.usersigninview, name='user'),
    path('google/login/callback', views.googlecallbackview, name = 'google-callback'),
    path('logout/', views.userlogoutview, name='logout'),
    path('profile/', views.userprofileview, name='user-profile'),
    path('account-deleted/', views.userdeleteview, name='user-deleted'),
]