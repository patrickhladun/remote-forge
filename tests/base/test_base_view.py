import pytest
from bs4 import BeautifulSoup
from django.test import Client
from django.urls import reverse

from tests.factories import TalentFactory


@pytest.mark.django_db
def test_home_page_renders_correctly():
    client = Client()
    response = client.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_page_renders_correctly():
    client = Client()
    response = client.get(reverse("about"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_page_renders_correctly():
    client = Client()
    response = client.get(reverse("contact"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_seccess_page_renders_correctly():
    client = Client()
    response = client.get(reverse("contact_success"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_jobs_page_renders_correctly():
    client = Client()
    response = client.get(reverse("job-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_talents_page_renders_correctly():
    client = Client()
    response = client.get(reverse("talents"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_employers_page_renders_correctly():
    client = Client()
    response = client.get(reverse("employers"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_privacy_policy_page_renders_correctly():
    client = Client()
    response = client.get(reverse("privacy"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_terms_of_service_page_renders_correctly():
    client = Client()
    response = client.get(reverse("terms"))
    assert response.status_code == 200
