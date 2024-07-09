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
    """
    View function to display a specific job and its associated employer.

    This function retrieves a job and its employer based on the provided
    job ID. It also fetches all published jobs for the employer. Metadata for
    the job page is generated and included in the context data.

    Args:
        request: The HTTP request object.
        id (int): The ID of the job to be retrieved.

    Returns:
        HttpResponse: The rendered job page with job details, employer details,
        associated published jobs, and metadata.

    Raises:
        Http404: If the job or employer does not exist.
    """
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
            "title": f"{title_job}{title_company}{title_in}{title_city}"
            f"{title_comma}{title_country}",
            "meta": {
                "description": "Remote Forge is a platform that connects "
                "remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online "
                "Jobs, Remote Talents",
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
    """
    View function to display a list of published jobs and their associated
    employers.

    This function retrieves all published jobs and filters them based on the
    keyword and location provided in the GET parameters. It also generates
    metadata for the job list page and prepares a list of job and employer
    data to be rendered on the page.

    Args:
        request: The HTTP request object containing optional GET parameters
        'keyword' and 'location'.

    Returns:
        HttpResponse: The rendered job list page with job and employer details,
        filter form, keyword, and metadata.
    """
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
                "description": "Remote Forge is a platform that connects "
                "remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online "
                "Jobs, Remote Talents",
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
    """
    View function for user-specific job listings.

    This function displays a list of jobs associated with the logged-in user.
    It checks if the user is of type "employer" and raises a PermissionDenied
    exception if not.

    Args:
        request: The HTTP request object from the logged-in user.

    Returns:
        HttpResponse: The rendered user job list page with the user's jobs.
    """

    metadata = make_metadata(
        request,
        {
            "title": "My Jobs",
        },
    )

    if request.user.user_type != "employer":
        raise PermissionDenied
    jobs = Job.objects.filter(user=request.user)

    data = {
        "jobs": jobs,
        "metadata": metadata,
    }

    return render(request, "job/user/job_list.html", data)


@login_required
def user_job_add(request):
    """
    View function for adding a job listing by a user.

    This function allows an employer user to add a new job listing. It checks
    if the user is of type "employer" and raises a PermissionDenied exception
    if not. If the request method is POST, it processes the job form and saves
    the job listing. On successful addition, it redirects to the user job list
    page with a success message. If the request method is GET, it displays an
    empty job form.

    Args:
        request: The HTTP request object from the logged-in user.

    Returns:
        HttpResponse: The rendered job add page with the job form.
    """
    if request.user.user_type != "employer":
        raise PermissionDenied

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, "Job listing added successfully.")
            return redirect("user-job-list")
    else:
        form = JobForm()

    return render(request, "job/user/job_add.html", {"form": form})


@login_required
def user_job_edit(request, id):
    """
    View function for editing a job listing by a user.

    This function allows an employer user to edit an existing job listing. It
    checks if the user is the owner of the job listing and raises a
    PermissionDenied exception if not. If the request method is POST, it
    processes the job form and updates the job listing. On successful update,
    it displays the job edit page with a success message. If the request
    method is GET, it displays the job form pre-filled with the existing job
    data.

    Args:
        request: The HTTP request object from the logged-in user.
        id: The ID of the job listing to be edited.

    Returns:
        HttpResponse: The rendered job edit page with the job form.
    """
    job = get_object_or_404(Job, id=id)

    if job.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job listing updated successfully.")
            return render(
                request, "job/user/job_edit.html", {"form": form, "job": job}
            )
    else:
        form = JobForm(instance=job)

    return render(
        request, "job/user/job_edit.html", {"form": form, "job": job}
    )


@login_required
def delete_job(request, id):
    """
    View function for deleting a job listing.

    This function allows an employer user to delete a job listing. It checks
    if the user is the owner of the job listing and raises a PermissionDenied
    exception if not. If the request method is POST, it deletes the job
    listing and redirects to the user job list page with a success message.
    If the request method is not POST, it simply redirects to the user job
    list page.

    Args:
        request: The HTTP request object from the logged-in user.
        id: The ID of the job listing to be deleted.

    Returns:
        HttpResponse: Redirects to the user job list page.
    """

    job = get_object_or_404(Job, id=id)

    if job.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("user-job-list")

    return redirect("user-job-list")
