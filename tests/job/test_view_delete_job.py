import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.test import Client
from django.urls import reverse

from apps.job.models import Job
from tests.factories import EmployerFactory, JobFactory, UserEmployerFactory

User = get_user_model()


@pytest.mark.django_db
def test_delete_job_as_owner():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("dhHf5edR?IDhhqkgGr")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)
    job = JobFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.post(reverse("delete-job", kwargs={"id": job.id}))
    assert response.status_code == 302
    assert not Job.objects.filter(id=job.id).exists()


@pytest.mark.django_db
def test_delete_job_as_non_owner():
    client = Client()

    owner_user = UserEmployerFactory()
    owner_user.set_password("&dVXuFEIocpSW6F1@X")
    owner_user.save()

    non_owner_user = UserEmployerFactory()
    non_owner_user.set_password("qJEIv06qOh59xqNb!K")
    non_owner_user.save()

    owner_employer = EmployerFactory(user=owner_user)
    non_owner_employer = EmployerFactory(user=non_owner_user)
    job = JobFactory(user=owner_user)

    client.force_login(non_owner_user)

    response = client.post(reverse("delete-job", kwargs={"id": job.id}))
    assert response.status_code == 403
    assert Job.objects.filter(id=job.id).exists()
