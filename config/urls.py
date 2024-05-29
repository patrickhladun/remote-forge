from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.user.views import talent_signup_view, employer_signup_view

urlpatterns = [
    path('', include('apps.base.urls')),
    path('', include('apps.job.urls')),
    path('', include('apps.user.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("accounts/signup/talent/", talent_signup_view, name="talent_signup"),
    path("accounts/signup/employer/", employer_signup_view, name="employer_signup",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
