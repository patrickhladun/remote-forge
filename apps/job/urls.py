from django.urls import path
from . import views

urlpatterns = [
    path("job/<uuid:id>", views.job, name="job"),
    path("jobs/", views.jobs, name="jobs"),
]
