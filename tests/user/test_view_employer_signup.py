import pytest
from allauth.account.models import EmailAddress
from django.test import Client
from django.urls import reverse

from apps.user.forms import EmployerSignupForm
from apps.user.models import User
from tests.factories import EmployerFactory, UserEmployerFactory


@pytest.mark.django_db
def test_employer_signup_view_get():
    client = Client()

    response = client.get(reverse("employer_signup"))
    assert response.status_code == 200
    assert isinstance(response.context["form"], EmployerSignupForm)


@pytest.mark.django_db
def test_employer_signup_view_post_valid():
    client = Client()
    data = {
        "email": "johndoe@example.com",
        "username": "johndoe",
        "password1": "AvZ!Q%Z9R!qnG+CzlX",
        "password2": "AvZ!Q%Z9R!qnG+CzlX",
    }

    response = client.post(reverse("employer_signup"), data)
    assert response.status_code == 302
    assert response.url == reverse("welcome")

    user = User.objects.get(username="johndoe")
    assert user.email == "johndoe@example.com"

    response = client.get(reverse("welcome"))
    assert response.status_code == 200
    assert "_auth_user_id" in client.session
    assert client.session["user_type"] == "employer"


@pytest.mark.django_db
def test_employer_signup_view_post_invalid():
    client = Client()
    data = {
        "email": "invalid-email",
        "username": "johndoe",
        "password1": "UYx?x8M@?zFeSHBD6H",
        "password2": "UYx?x8M@?zFeSHBD6H",
    }

    response = client.post(reverse("employer_signup"), data)
    assert response.status_code == 200
    assert isinstance(response.context["form"], EmployerSignupForm)
    assert response.context["form"].errors
