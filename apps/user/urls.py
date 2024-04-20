from django.urls import path, register_converter
from django.urls import path
from . import views

urlpatterns = [
  path('talent/<uuid:id>', views.talent, name='talent'),
  path('talents/', views.talents, name='talents'),
]