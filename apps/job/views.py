from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import JobListingForm


def job(request, id):
    """View function for job."""
    job_obj = get_object_or_404(Listing, id=id)

    if hasattr(job_obj.user, "employer"):
        employer = job_obj.user.employer
        employer_name = employer.company

    job_obj.employer = employer_name

    return render(request, "job/job.html", {"job": job_obj})


def jobs(request):
    """View function for jobs."""
    jobs = Listing.objects.all()
    return render(request, "job/jobs.html", {"jobs": jobs})


def my_jobs(request):
    """View function for jobs."""
    jobs = Listing.objects.all()
    return render(request, "job/admin/my_jobs.html", {"jobs": jobs})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user = request.user  # Set the user as the current logged-in user
            new_listing.save()
            return redirect('my-jobs')  # Redirect to a confirmation page or listings overview
    else:
        form = JobListingForm()

    return render(request, 'job/admin/add_job.html', {"form": form})


