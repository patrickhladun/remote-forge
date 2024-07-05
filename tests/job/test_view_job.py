import uuid

import pytest
from django.shortcuts import get_object_or_404
from django.test import Client
from django.urls import reverse

from apps.job.models import Job
from apps.user.models import Employer


@pytest.mark.django_db
def test_job_view(test_data_single_job):
    client = Client()

    job = test_data_single_job

    response = client.get(reverse("job", args=[job.id]))
    assert response.status_code == 200

    assert "job/job.html" in (t.name for t in response.templates)

    job_obj = get_object_or_404(Job, id=job.id)
    employer = get_object_or_404(Employer, user=job_obj.user)
    jobs = Job.objects.filter(user=job_obj.user, is_published=True)

    assert list(response.context["jobs"]) == list(jobs)

    assert response.context["job"] == job_obj
    assert response.context["job"].title == job.title
    assert response.context["job"].city == job.city
    assert response.context["job"].country == job.country
    assert response.context["job"].salary == job.salary
    assert response.context["job"].schedule == job.schedule
    assert response.context["job"].is_published == job.is_published
    assert response.context["job"].details == job.details

    assert response.context["employer"] == employer
    assert response.context["employer"].first_name == employer.first_name
    assert response.context["employer"].last_name == employer.last_name
    assert response.context["employer"].phone == employer.phone
    assert response.context["employer"].company == employer.company
    assert response.context["employer"].about == employer.about
    assert response.context["employer"].website == employer.website
    assert response.context["employer"].city == employer.city
    assert response.context["employer"].country == employer.country


@pytest.mark.django_db
def test_job_view_non_existing_id():
    client = Client()

    non_existing_job_id = uuid.uuid4()

    response = client.get(reverse("job", args=[non_existing_job_id]))
    assert response.status_code == 404
