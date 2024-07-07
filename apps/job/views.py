from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.dateparse import parse_date

from apps.user.models import Employer
from common.utils.metadata import make_metadata

from .forms import JobForm, JobsFilterForm
from .models import Job


def job(request, id):
    """View function for job."""
    job = get_object_or_404(Job, id=id)
    employer = get_object_or_404(Employer, user=job.user)
    jobs = Job.objects.filter(user=job.user, is_published=True)

    title_job = job.title or "Job"
    title_company = f" at {employer.company}" if employer.company else ""
    title_in = " in " if job.city or job.country else ""
    title_city = f"{job.city}" if job.city else ""
    title_comma = ", " if job.city and job.country else ""
    title_country = f"{employer.country}" if employer.country else ""

    metadata = make_metadata(
        request,
        {
            "title": f"{title_job}{title_company}{title_in}{title_city}{title_comma}{title_country}",
            "meta": {
                "description": "Remote Forge is a platform that connects remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs, Remote Talents",
                "robots": "index, follow",
            },
        },
    )

    data = {
        "job": job,
        "employer": employer,
        "jobs": jobs,
        "metadata": metadata,
    }

    return render(request, "job/job.html", data)


def job_list(request):
    """View function for jobs."""
    keyword = request.GET.get("keyword", "")
    location = request.GET.get("location", "")
    jobs = Job.objects.filter(is_published=True)
    jobs_filter_form = JobsFilterForm(request.GET)
    data = []

    metadata = make_metadata(
        request,
        {
            "title": "Jobs List | Find Your Perfect Remote Job",
            "meta": {
                "description": "Remote Forge is a platform that connects remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs, Remote Talents",
                "robots": "index, follow",
            },
        },
    )

    if keyword:
        jobs = jobs.filter(title__icontains=keyword)

    for job in jobs:
        employer = get_object_or_404(Employer, user=job.user)

        if location:
            if (
                job.city.lower() == location.lower()
                or job.country.lower() == location.lower()
            ):
                data.append({"job": job, "employer": employer})
        else:
            data.append({"job": job, "employer": employer})

    data = {
        "data": data,
        "jobs_filter_form": jobs_filter_form,
        "keyword": keyword,
        "metadata": metadata,
    }

    return render(request, "job/job_list.html", data)


@login_required
def user_job_list(request):
    """View function for user-specific job listings."""
    if request.user.user_type != "employer":
        raise PermissionDenied
    jobs = Job.objects.filter(user=request.user)
    return render(request, "job/user/job_list.html", {"jobs": jobs})


@login_required
def user_job_add(request):
    if request.user.user_type != "employer":
        raise PermissionDenied

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect("user-job-list")
    else:
        form = JobForm()

    return render(request, "job/user/job_add.html", {"form": form})


@login_required
def user_job_edit(request, id):
    job = get_object_or_404(Job, id=id)

    if job.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job listing updated successfully.")
            return render(request, "job/user/job_edit.html", {"form": form, "job": job})
    else:
        form = JobForm(instance=job)

    return render(request, "job/user/job_edit.html", {"form": form, "job": job})


@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    if job.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("user-job-list")

    return redirect("user-job-list")
