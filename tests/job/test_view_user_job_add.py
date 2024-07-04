import uuid

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from apps.job.forms import JobForm
from apps.job.models import Job
from tests.factories import (
    EmployerFactory,
    TalentFactory,
    UserEmployerFactory,
    UserTalentFactory,
)


@pytest.mark.django_db
def test_user_job_add_user_visitor():
    client = Client()

    response = client.get(reverse("user-job-add"))
    assert response.status_code == 302
    assert "/accounts/login/" in response.url


@pytest.mark.django_db
def test_user_job_add_user_employer():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("password")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("user-job-add"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_job_add_user_employer_form_success():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("2C?&DBSOb2dMLwNlPd")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("user-job-add"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, JobForm)

    data = {
        "is_published": True,
        "title": "Test Job",
        "city": "City",
        "salary": "Salary",
        "schedule": "Schedule",
        "details": '[{"heading": "Job Description", "content": "Test"}]',
    }

    response = client.post(reverse("user-job-add"), data)
    assert response.status_code == 302

    job = Job.objects.first()
    assert job.user == employer_user
    assert job.title == "Test Job"
    assert job.city == "City"
    assert job.salary == "Salary"
    assert job.schedule == "Schedule"
    assert job.details == [{"heading": "Job Description", "content": "Test"}]


@pytest.mark.django_db
def test_user_job_add_user_employer_form_fail_not_title():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("rv5gQ$KjTF&sy4BlDG")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("user-job-add"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, JobForm)

    data = {
        "title": "",
    }

    response = client.post(reverse("user-job-add"), data)
    assert response.status_code == 200

    form = response.context["form"]
    assert not form.is_valid()
    assert "title" in form.errors


@pytest.mark.django_db
def test_user_job_add_user_talent():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("password")
    talent_user.save()

    talent = EmployerFactory(user=talent_user)

    client.force_login(talent_user)

    response = client.get(reverse("user-job-add"))
    assert response.status_code == 403
