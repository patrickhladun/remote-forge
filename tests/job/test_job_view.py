import pytest
from django.test import Client
from django.urls import reverse

from apps.job.models import Job
from apps.user.models import User
from tests.factories import EmployerFactory, JobFactory, UserEmployerFactory


@pytest.fixture
def test_data():
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

    return job1, job2, job3, job4


@pytest.mark.django_db
def test_job_list_view_no_filters(test_data):
    """Test job list view without filters. Unpublished jobs should not be displayed."""
    client = Client()

    response = client.get(reverse("job-list"))
    assert response.status_code == 200
    assert len(response.context["data"]) == 3


@pytest.mark.django_db
def test_job_list_view_location_filter_not_existing(test_data):
    """Test job list view with location filter that does not exist."""
    client = Client()

    response = client.get(reverse("job-list") + "?location=NotExisting")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0


@pytest.mark.django_db
def test_job_list_view_location_filter_warsaw(test_data):
    """Test job list view with location filter Warsaw."""
    client = Client()

    response = client.get(reverse("job-list") + "?location=Warsaw")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1
    assert response.context["data"][0]["job"].title == "Backend Developer"
    assert response.context["data"][0]["job"].city == "Warsaw"
    # Ensure the test checks the job's city, not the employer's city for filtering
    assert response.context["data"][0]["employer"].city == "Krakow"
    assert response.context["data"][0]["job"].country == "Poland"


@pytest.mark.django_db
def test_job_list_view_location_filter_dublin(test_data):
    client = Client()

    response = client.get(reverse("job-list") + "?location=Dublin")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1


@pytest.mark.django_db
def test_job_list_view_location_filter_galway(test_data):
    client = Client()

    response = client.get(reverse("job-list") + "?location=Galway")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1


@pytest.mark.django_db
def test_job_list_view_location_filter_ireland(test_data):
    client = Client()

    response = client.get(reverse("job-list") + "?location=Ireland")
    assert response.status_code == 200
    assert len(response.context["data"]) == 2


@pytest.mark.django_db
def test_job_list_view_location_filter_cork(test_data):
    """Test job list view with location filter that does not exist."""
    client = Client()

    response = client.get(reverse("job-list") + "?location=Cork")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0
