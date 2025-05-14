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

from shortener import views


urlpatterns = [
    # 127.0.0.1:8000/ -> home_view() -> html
    path("", views.home_view, name="home"),

    # 127.0.0.1:8000/short-urls/ -> short_url_create_view()
    path("short-urls/", views.short_url_create_view, name="shorten_url"),

    # 127.0.0.1:8000/admin/ -> admin.site.urls
    path('admin/', admin.site.urls),

    # 127.0.0.1:8000/aabcd/
    path("<str:code>/", views.redirect_view, name="short_url_redirect"),
]
