from django.urls import path
from . import views

urlpatterns = [
  path('talents/', views.talents_view, name='talents'),
  path('talent/<uuid:id>', views.talent_view, name='talent'),
  path('account/', views.account_view, name='account'),
  path('profile/', views.profile_view, name='profile'),
]