import uuid

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from apps.job.forms import JobForm
from apps.job.models import Job
from tests.factories import (
    EmployerFactory,
    JobFactory,
    TalentFactory,
    UserEmployerFactory,
    UserTalentFactory,
)


@pytest.mark.django_db
def test_user_job_add_user_visitor():
    client = Client()

    response = client.get(reverse("user-job-edit", kwargs={"id": uuid.uuid4()}))
    assert response.status_code == 302
    assert "/accounts/login/" in response.url


@pytest.mark.django_db
def test_user_job_edit_user_employer():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("mfH$VnqN?jTMwDH4PQ")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)
    job = JobFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("user-job-edit", kwargs={"id": job.id}))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, JobForm)

    data = {
        "title": "Updated Job Title",
        "city": job.city,
        "country": job.country,
        "salary": job.salary,
        "schedule": job.schedule,
        "details": job.details,
    }
    response = client.post(reverse("user-job-edit", kwargs={"id": job.id}), data)
    assert response.status_code == 302

    updated_job = Job.objects.get(id=job.id)
    assert updated_job.title == "Updated Job Title"
