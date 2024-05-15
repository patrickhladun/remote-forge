from django.urls import path
from . import views

urlpatterns = [
    path("job/<uuid:id>", views.job, name="job"),
    path("jobs/", views.jobs, name="jobs"),
    path("my-jobs/", views.my_jobs, name="my-jobs"),
    path("add-job/", views.add_job, name="add-job"),
]
