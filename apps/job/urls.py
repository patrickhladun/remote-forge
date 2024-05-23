from django.urls import path
from . import views

urlpatterns = [
    path("job/<uuid:id>", views.job, name="job"),
    path("job-list/", views.job_list, name="job-list"),
    path("user-job-list/", views.user_job_list, name="user-job-list"),
    path("user-job-add/", views.user_job_add, name="user-job-add"),
    path("user-job-edit/<uuid:id>", views.user_job_edit, name="user-job-edit"),
]
 