import pytest
from django.test import Client
from django.urls import Resolver404, resolve, reverse

from apps.base import views


@pytest.mark.django_db
class TestURLs:
    def test_home_url_resolves(self):
        url = reverse("home")
        assert resolve(url).func == views.home

    def test_about_url_resolves(self):
        url = reverse("about")
        assert resolve(url).func == views.about

    def test_contact_url_resolves(self):
        url = reverse("contact")
        assert resolve(url).func == views.contact

    def test_contact_success_url_resolves(self):
        url = reverse("contact_success")
        assert resolve(url).func == views.contact_success

    def test_privacy_url_resolves(self):
        url = reverse("privacy")
        assert resolve(url).func == views.privacy

    def test_terms_url_resolves(self):
        url = reverse("terms")
        assert resolve(url).func == views.terms


@pytest.mark.django_db
class TestStatusCodes:
    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse("home"))
        assert response.status_code == 200

    def test_about_status_code(self):
        client = Client()
        response = client.get(reverse("about"))
        assert response.status_code == 200

    def test_contact_status_code(self):
        client = Client()
        response = client.get(reverse("contact"))
        assert response.status_code == 200

    def test_contact_success_status_code(self):
        client = Client()
        response = client.get(reverse("contact_success"))
        assert response.status_code == 200

    def test_privacy_status_code(self):
        client = Client()
        response = client.get(reverse("privacy"))
        assert response.status_code == 200

    def test_terms_status_code(self):
        client = Client()
        response = client.get(reverse("terms"))
        assert response.status_code == 200

    def test_invalid_url(self):
        with pytest.raises(Resolver404):
            resolve("/invalid_url/")
