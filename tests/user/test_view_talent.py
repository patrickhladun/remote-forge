import json
import uuid

import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import TalentFactory, UserTalentFactory


@pytest.mark.django_db
def test_talent_view():
    client = Client()

    talent_user = UserTalentFactory()
    talent_user.set_password("Vxc#geo!@aOSj0sUZj")
    talent_user.save()

    talent = TalentFactory(user=talent_user)

    response = client.get(reverse("talent", kwargs={"id": talent.id}))
    assert response.status_code == 200
    assert str(response.context["talent"].pk) == str(talent.pk)
    assert response.context["talent"].is_published == talent.is_published
    assert response.context["talent"].first_name == talent.first_name
    assert response.context["talent"].last_name == talent.last_name
    assert response.context["talent"].phone == talent.phone
    assert response.context["talent"].bio == talent.bio
    assert response.context["talent"].website == talent.website
    assert response.context["talent"].city == talent.city
    assert response.context["talent"].country == talent.country
    assert response.context["talent"].experience == talent.experience
    assert response.context["talent"].education == talent.education
    assert response.context["talent"].skills == talent.skills
    assert response.context["talent"].interests == talent.interests
    assert response.context["talent"].social == talent.social


@pytest.mark.django_db
def test_talent_view_non_existing_id():
    client = Client()

    non_existing_talent_id = uuid.uuid4()

    response = client.get(reverse("talent", args=[non_existing_talent_id]))
    assert response.status_code == 404
