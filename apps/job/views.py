from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import JobForm


def job(request, id):
    """View function for job."""
    job_obj = get_object_or_404(Job, id=id)

    if hasattr(job_obj.user, "employer"):
        employer = job_obj.user.employer
        employer_name = employer.company

    job_obj.employer = employer_name

    return render(request, "job/job.html", {"job": job_obj})


def job_list(request):
    """View function for jobs."""
    jobs = Job.objects.all()
    return render(request, "job/job_list.html", {"jobs": jobs})


@login_required
def user_job_list(request):
    """View function for user-specific job listings."""
    # Filter the listings to only those created by the logged-in user
    jobs = Job.objects.filter(user=request.user)
    return render(request, "job/user/job_list.html", {"jobs": jobs})


@login_required
def user_job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user = request.user  # Set the user as the current logged-in user
            new_listing.save()
            return redirect('user-job-list')  # Redirect to a confirmation page or listings overview
    else:
        form = JobForm()

    return render(request, 'job/user/job_add.html', {"form": form})


@login_required
def user_job_update(request):
    return render(request, 'job/user/job_update.html')

