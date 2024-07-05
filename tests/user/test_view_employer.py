import uuid

import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import EmployerFactory, JobFactory, UserEmployerFactory


@pytest.mark.django_db
def test_employer_view():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("$m#ojY5lI@4On5!TgI")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    job1 = JobFactory(user=employer_user, is_published=True)
    job2 = JobFactory(user=employer_user, is_published=True)
    job3 = JobFactory(user=employer_user, is_published=False)

    response = client.get(reverse("employer", kwargs={"id": employer.id}))
    assert response.status_code == 200
    assert str(response.context["employer"].pk) == str(employer.pk)
    assert response.context["employer"].first_name == employer.first_name
    assert response.context["employer"].last_name == employer.last_name
    assert response.context["employer"].phone == employer.phone
    assert response.context["employer"].company == employer.company
    assert response.context["employer"].about == employer.about
    assert response.context["employer"].website == employer.website
    assert response.context["employer"].city == employer.city
    assert response.context["employer"].country == employer.country

    assert len(response.context["jobs"]) == 2

    jobs = response.context["jobs"]
    job_pks = [str(job.pk) for job in jobs]
    assert str(job1.pk) in job_pks
    assert str(job2.pk) in job_pks
    assert str(job3.pk) not in job_pks


@pytest.mark.django_db
def test_employer_view_non_existing_id():
    client = Client()

    non_existing_employer_id = uuid.uuid4()

    response = client.get(reverse("employer", args=[non_existing_employer_id]))
    assert response.status_code == 404
