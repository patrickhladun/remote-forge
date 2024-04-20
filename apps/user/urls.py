from django.urls import path, register_converter
from django.urls import path
from . import views

urlpatterns = [
  path('talent/', views.talent, name='talent'),
  path('talent-profile/<uuid:id>', views.talent_profile, name='talent-profile'),
]