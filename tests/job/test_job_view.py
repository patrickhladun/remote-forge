import pytest
from django.test import Client
from django.urls import reverse

from apps.job.models import Job
from apps.user.models import User
from tests.factories import EmployerFactory, JobFactory, UserEmployerFactory


@pytest.mark.django_db
def test_job_list_view():
    client = Client()

    employer_user_1 = UserEmployerFactory()
    employer_1 = EmployerFactory(user=employer_user_1, city="Dublin")

    employer_user_2 = UserEmployerFactory()
    employer_2 = EmployerFactory(user=employer_user_2, city="Galway")

    employer_user_3 = UserEmployerFactory()
    employer_3 = EmployerFactory(user=employer_user_3, city="Krakow")

    job1 = JobFactory(
        user=employer_user_1,
        title="DevOps Engineer",
        city="Dublin",
        country="Ireland",
        is_published=True,
    )
    job2 = JobFactory(
        user=employer_user_2,
        title="Frontend Developer",
        city="Galway",
        country="Ireland",
        is_published=True,
    )
    job3 = JobFactory(
        user=employer_user_3,
        title="Backend Developer",
        city="Warsaw",
        country="Poland",
        is_published=True,
    )
    job4 = JobFactory(
        user=employer_user_3,
        title="Backend Developer",
        city="Wroclaw",
        country="Poland",
        is_published=False,
    )

    # Test without filters (all jobs)
    # Unpublished job should not be visible
    response = client.get(reverse("job-list"))
    assert response.status_code == 200
    print("Response context data (no filters):", response.context["data"])
    assert len(response.context["data"]) == 3

    # Test with keyword filter
    response = client.get(reverse("job-list") + "?keyword=DevOps")
    job = response.context["data"][0]["job"]
    assert response.status_code == 200
    assert len(response.context["data"]) == 1
    assert job.title == "DevOps Engineer"
    assert job.city == "Dublin"

    # Test with filter location Dublin
    response = client.get(reverse("job-list") + "?location=Dublin")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1

    # Test with filter location Galway
    response = client.get(reverse("job-list") + "?location=Galway")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1

    # Test with filter location Warsaw
    response = client.get(reverse("job-list") + "?keyword=&location=Warsaw")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1
    assert response.context["data"][0]["job"].title == "Backend Developer"
    assert response.context["data"][0]["job"].city == "Warsaw"
    assert response.context["data"][0]["employer"].city == "Krakow"

    # Test with filter location Ireland
    response = client.get(reverse("job-list") + "?location=Ireland")
    assert response.status_code == 200
    assert len(response.context["data"]) == 2

    # Test with filter location Cork
    response = client.get(reverse("job-list") + "?location=Cork")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0

    # Test for not existing location keyword
    response = client.get(reverse("job-list") + "?location=NotExisting")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0
