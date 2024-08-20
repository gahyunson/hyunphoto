from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='user'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.UserProfileAPI.as_view(), name='user-profile'),
]