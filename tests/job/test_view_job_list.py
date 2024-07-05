import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_job_list_view_no_filters(test_data_jobs):
    """Test job list view without filters. Unpublished jobs should not be displayed."""
    client = Client()
    response = client.get(reverse("job-list"))
    assert response.status_code == 200
    assert len(response.context["data"]) == 3


@pytest.mark.django_db
def test_job_list_view_location_filter_not_existing(test_data_jobs):
    """Test job list view with location filter that does not exist."""
    client = Client()
    response = client.get(reverse("job-list") + "?location=NotExisting")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0


@pytest.mark.django_db
def test_job_list_view_location_filter_warsaw(test_data_jobs):
    """Test job list view with location filter Warsaw."""
    client = Client()
    job1, job2, job3, job4 = test_data_jobs
    response = client.get(reverse("job-list") + "?location=Warsaw")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1
    assert response.context["data"][0]["job"].title == "Backend Developer"
    assert response.context["data"][0]["job"].city == "Warsaw"
    # Ensure the test checks the job's city, not the employer's city for filtering
    assert response.context["data"][0]["employer"].city == "Krakow"
    assert response.context["data"][0]["job"].country == "Poland"


@pytest.mark.django_db
def test_job_list_view_location_filter_dublin(test_data_jobs):
    client = Client()
    response = client.get(reverse("job-list") + "?location=Dublin")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1


@pytest.mark.django_db
def test_job_list_view_location_filter_galway(test_data_jobs):
    client = Client()
    response = client.get(reverse("job-list") + "?location=Galway")
    assert response.status_code == 200
    assert len(response.context["data"]) == 1


@pytest.mark.django_db
def test_job_list_view_location_filter_ireland(test_data_jobs):
    client = Client()
    response = client.get(reverse("job-list") + "?location=Ireland")
    assert response.status_code == 200
    assert len(response.context["data"]) == 2


@pytest.mark.django_db
def test_job_list_view_location_filter_cork(test_data_jobs):
    """Test job list view with location filter that does not exist."""
    client = Client()
    response = client.get(reverse("job-list") + "?location=Cork")
    assert response.status_code == 200
    assert len(response.context["data"]) == 0
