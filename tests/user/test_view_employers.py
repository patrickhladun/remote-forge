import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import EmployerFactory


@pytest.mark.django_db
def test_employers_view():
    client = Client()

    response = client.get(reverse("employers"))
    assert response.status_code == 200
    assert response.context["employers"].count() == 0
    assert response.context["employers"].exists() == False

    EmployerFactory(is_published=True)
    EmployerFactory(is_published=True)
    EmployerFactory(is_published=False)

    response = client.get(reverse("employers"))
    assert response.status_code == 200
    assert response.context["employers"].count() == 2
    assert response.context["employers"].exists() == True
