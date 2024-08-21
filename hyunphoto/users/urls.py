from django.urls import path
from . import views 

urlpatterns = [
    path('', views.usersigninview, name='user'),
    path('logout/', views.userlogoutview, name='logout'),
    path('profile/', views.userprofileview, name='user-profile'),
]