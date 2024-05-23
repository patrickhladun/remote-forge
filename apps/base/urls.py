from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-conditions/', views.terms, name='terms'),
]