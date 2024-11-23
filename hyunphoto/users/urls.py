from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.usersigninview, name='login'),
    path('callback/', views.googlecallbackview, name = 'google-callback'),
    # path('logout/', views.userlogoutview, name='logout'),
    path('profile/', views.userprofileview, name='user-profile'),
    path('account-deleted/', views.userdeleteview, name='user-deleted'),
]