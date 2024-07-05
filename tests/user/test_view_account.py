import pytest
from django.test import Client
from django.urls import reverse

from apps.user.forms import AccountProfile
from apps.user.models import User
from tests.factories import UserEmployerFactory, UserTalentFactory


@pytest.mark.django_db
def test_employer_account_view():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("JSlVNcoE+nosQObR5#")
    employer_user.save()

    client.force_login(employer_user)

    response = client.get(reverse("account"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, AccountProfile)
    assert form.instance == employer_user


@pytest.mark.django_db
def test_talent_account_view():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("tkvU55W2Uwyb4tEKy3")
    talent_user.save()

    client.force_login(talent_user)

    response = client.get(reverse("account"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, AccountProfile)
    assert form.instance == talent_user


@pytest.mark.django_db
def test_employer_account_view_post_valid():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("M5mvLgwwyN8d3jAu5w")
    employer_user.save()

    client.force_login(employer_user)

    data = {
        "email": "newemployeremail@example.com",
        "username": employer_user.username,
    }

    response = client.post(reverse("account"), data)
    assert response.status_code == 200

    employer_user.refresh_from_db()
    assert employer_user.email == "newemployeremail@example.com"


@pytest.mark.django_db
def test_talent_account_view_post_valid():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("Zzu8vyzcFTQeVbsUst")
    talent_user.save()

    client.force_login(talent_user)

    data = {
        "email": "newtalentemail@example.com",
        "username": talent_user.username,
    }

    response = client.post(reverse("account"), data)
    assert response.status_code == 200

    talent_user.refresh_from_db()
    assert talent_user.email == "newtalentemail@example.com"


@pytest.mark.django_db
def test_employer_account_view_post_invalid():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("fi9%k#NAAPLrV83E7")
    employer_user.save()

    client.force_login(employer_user)

    data = {
        "email": "invalid-email",
        "username": employer_user.username,
    }

    response = client.post(reverse("account"), data)
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, AccountProfile)
    assert form.errors


@pytest.mark.django_db
def test_talent_account_view_post_invalid():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("mxN9ozfUgUPK&XE+y2")
    talent_user.save()

    client.force_login(talent_user)

    data = {
        "email": "invalid-email",
        "username": talent_user.username,
    }

    response = client.post(reverse("account"), data)
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, AccountProfile)
    assert form.errors
