from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from apps.user.views import employer_signup_view, talent_signup_view


def custom_404(request, exception):
    return render(request, "404.html", status=404)


handler404 = custom_404

urlpatterns = [
    path("", include("apps.base.urls")),
    path("", include("apps.job.urls")),
    path("", include("apps.user.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/signup/talent/", talent_signup_view, name="talent_signup"),
    path(
        "accounts/signup/employer/",
        employer_signup_view,
        name="employer_signup",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
