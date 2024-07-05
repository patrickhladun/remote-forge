import pytest
from django.test import Client
from django.urls import reverse

from apps.user.forms import AccountProfile, EmployerProfileForm, TalentProfileForm
from apps.user.models import User
from tests.factories import (
    EmployerFactory,
    TalentFactory,
    UserEmployerFactory,
    UserTalentFactory,
)


@pytest.mark.django_db
def test_welcome_view_not_authenticated():
    client = Client()

    response = client.get(reverse("welcome"))
    assert response.status_code == 302
    assert response.url.startswith(reverse("account_login") + "?next=")


@pytest.mark.django_db
def test_welcome_view_as_talent():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("mL?DE?iR78T@DYPJUz")
    talent_user.save()

    talent = TalentFactory(user=talent_user)

    client.force_login(talent_user)

    response = client.get(reverse("welcome"))
    assert response.status_code == 200
    assert response.context["user_type"] == "talent"


@pytest.mark.django_db
def test_welcome_view_as_employer():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("J&A3R7i5&T?mDSG7936")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("welcome"))
    assert response.status_code == 200
    assert response.context["user_type"] == "employer"
