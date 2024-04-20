from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.base.urls')),
    path('', include('apps.user.urls')),
    path('admin/', admin.site.urls),
]
