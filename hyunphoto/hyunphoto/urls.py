"""
URL configuration for hyunphoto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# from core.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),

    path('', include('main.urls')),

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('users.urls')),

    path('api/photos/', include('photos.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/order/', include('order.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/fandq/', include('fandq.urls')),

    path('paypal/', include('paypal.standard.ipn.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)