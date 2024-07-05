import json

import pytest
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
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
def test_profile_view_not_authenticated():
    client = Client()

    response = client.get(reverse("profile"))
    assert response.status_code == 302
    assert response.url.startswith(reverse("account_login") + "?next=")


@pytest.mark.django_db
def test_profile_view_as_employer():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("JSlVNcoE+nosQObR5#")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    response = client.get(reverse("profile"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, EmployerProfileForm)
    assert str(form.instance.pk) == str(employer.pk)
    assert form.instance.user == employer.user
    assert form.instance.first_name == employer.first_name
    assert form.instance.last_name == employer.last_name


@pytest.mark.django_db
def test_profile_view_as_employer_form_submittion():
    client = Client()

    employer_user = UserEmployerFactory()
    employer_user.set_password("Ec95#ZiWY07TV1nga5")
    employer_user.save()

    employer = EmployerFactory(user=employer_user)

    client.force_login(employer_user)

    data = {
        "first_name": employer.first_name,
        "last_name": employer.last_name,
        "phone": employer.phone,
        "company": employer.company,
        "about": employer.about,
        "website": employer.website,
        "city": employer.city,
        "country": employer.country,
        "is_published": True,
    }

    response = client.post(reverse("profile"), data)

    assert response.status_code == 200
    assert employer.first_name == data["first_name"]
    assert employer.last_name == data["last_name"]
    assert employer.phone == data["phone"]
    assert employer.company == data["company"]
    assert employer.about == data["about"]
    assert employer.website == data["website"]
    assert employer.city == data["city"]
    assert employer.country == data["country"]
    assert employer.is_published == data["is_published"]


@pytest.mark.django_db
def test_profile_view_as_talent():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("#SNflvO@sEI!wkjQy7")
    talent_user.save()

    talent = TalentFactory(user=talent_user)

    client.force_login(talent_user)

    response = client.get(reverse("profile"))
    assert response.status_code == 200

    form = response.context["form"]
    assert isinstance(form, TalentProfileForm)
    assert str(form.instance.pk) == str(talent.pk)
    assert form.instance.user == talent.user
    assert form.instance.first_name == talent.first_name
    assert form.instance.last_name == talent.last_name


@pytest.mark.django_db
def test_profile_view_as_talent_form_submission():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("l+JlMhNQ2lyw&3a0vf")
    talent_user.save()

    talent = TalentFactory(user=talent_user)

    client.force_login(talent_user)

    resume_file = SimpleUploadedFile(
        "resume.pdf", b"file_content", content_type="application/pdf"
    )

    data = {
        "is_published": True,
        "first_name": talent.first_name,
        "last_name": talent.last_name,
        "phone": talent.phone,
        "bio": talent.bio,
        "resume": resume_file,
        "website": talent.website,
        "city": talent.city,
        "country": talent.country,
        "title": talent.title,
        "experience": json.dumps(talent.experience),
        "education": json.dumps(talent.education),
        "skills": json.dumps(talent.skills),
        "interests": talent.interests,
        "social": json.dumps(talent.social),
    }

    response = client.post(reverse("profile"), data)
    assert response.status_code == 200
    assert talent.is_published == data["is_published"]
    assert talent.first_name == data["first_name"]
    assert talent.last_name == data["last_name"]
    assert talent.phone == data["phone"]
    assert talent.bio == data["bio"]
    assert talent.website == data["website"]
    assert talent.city == data["city"]
    assert talent.country == data["country"]
    assert talent.title == data["title"]
    assert talent.experience == json.loads(data["experience"])
    assert talent.education == json.loads(data["education"])
    assert talent.skills == json.loads(data["skills"])
    assert talent.interests == data["interests"]
    assert talent.social == json.loads(data["social"])
