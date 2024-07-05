import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import TalentFactory


@pytest.mark.django_db
def test_talents_view():
    client = Client()

    response = client.get(reverse("talents"))
    assert response.status_code == 200
    assert response.context["talents"].count() == 0
    assert response.context["talents"].exists() == False

    TalentFactory(is_published=True)
    TalentFactory(is_published=True)
    TalentFactory(is_published=False)

    response = client.get(reverse("talents"))
    assert response.status_code == 200
    assert response.context["talents"].count() == 2
    assert response.context["talents"].exists() == True
