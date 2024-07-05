import pytest
from allauth.account.models import EmailAddress
from django.test import Client
from django.urls import reverse

from apps.user.forms import TalentSignupForm
from apps.user.models import User
from tests.factories import TalentFactory, UserTalentFactory


@pytest.mark.django_db
def test_talent_signup_view_get():
    client = Client()

    response = client.get(reverse("talent_signup"))
    assert response.status_code == 200
    assert isinstance(response.context["form"], TalentSignupForm)


@pytest.mark.django_db
def test_talent_signup_view_post_valid():
    client = Client()

    data = {
        "email": "johndoe@example.com",
        "username": "johndoe",
        "password1": "y5Vf1fK!ST$HRrkyXC",
        "password2": "y5Vf1fK!ST$HRrkyXC",
    }

    response = client.post(reverse("talent_signup"), data)
    assert response.status_code == 302
    assert response.url == reverse("welcome")

    user = User.objects.get(username="johndoe")
    assert user.email == "johndoe@example.com"

    response = client.get(reverse("welcome"))
    assert response.status_code == 200
    assert "_auth_user_id" in client.session
    assert client.session["user_type"] == "talent"


@pytest.mark.django_db
def test_talent_signup_view_post_invalid():
    client = Client()

    data = {
        "email": "invalid-email",
        "username": "johndoe",
        "password1": "ivdB5@6OZvpKwIoSC@",
        "password2": "ivdB5@6OZvpKwIoSC@",
    }

    response = client.post(reverse("talent_signup"), data)
    assert response.status_code == 200
    assert isinstance(response.context["form"], TalentSignupForm)
    assert response.context["form"].errors
