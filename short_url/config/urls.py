"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from shortener import views, apis


urlpatterns = [
    # Django 방식
    path("", views.home_view, name="home"),
    path("short-urls/", views.short_url_create_view, name="shorten_url"),
    path('admin/', admin.site.urls),
    path("<str:code>/", views.ShortURLDetailView.as_view(), name="short_url_detail"),

    # DRF 방식
    path("api/short-urls/", apis.ShortURLAPIView.as_view(), name="short_url_api"),
    path("api/generics/short-urls/", apis.ShortURLGenericAPIView.as_view()),
]
