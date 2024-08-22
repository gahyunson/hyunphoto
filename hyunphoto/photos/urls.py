from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='photos'),
    path('<int:photo_id>/', views.photodetailview, name='photo_detail'),
]