import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import (
    EmployerFactory,
    JobFactory,
    TalentFactory,
    UserEmployerFactory,
    UserTalentFactory,
)


@pytest.mark.django_db
def test_user_job_list_user_visitor():
    client = Client()

    response = client.get(reverse("user-job-list"))
    assert response.status_code == 302
    assert "/accounts/login/" in response.url


@pytest.mark.django_db
def test_user_job_list_user_employer():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("JBKzuu?HgzAfL9&B8Z")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)
    job1 = JobFactory(user=employer_user)
    job2 = JobFactory(user=employer_user)
    job3 = JobFactory(user=employer_user, is_published=False)

    client.force_login(employer_user)

    response = client.get(reverse("user-job-list"))
    assert response.status_code == 200
    assert len(response.context["jobs"]) == 3


@pytest.mark.django_db
def test_user_job_list_user_talent():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("tJ%H3DuPff$&@oh1Tk")
    talent_user.save()

    talent = EmployerFactory(user=talent_user)

    client.force_login(talent_user)

    response = client.get(reverse("user-job-list"))
    assert response.status_code == 403
