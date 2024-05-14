from django.shortcuts import get_object_or_404, render

from .models import Listing


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

