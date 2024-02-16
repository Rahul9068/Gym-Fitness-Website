from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    path('feature', views.feature, name= 'feature'),
    path('pricing', views.pricing, name= 'pricing'),
    path('banner', views.banner, name= 'banner'),
    path('blog', views.blog, name= 'blog'),
]