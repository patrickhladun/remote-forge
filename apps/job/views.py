from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    jobs = Job.objects.filter(is_published=True)
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
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('user-job-list') 
    else:
        form = JobForm()

    return render(request, 'job/user/job_add.html', {"form": form})


@login_required
def user_job_edit(request, id):
    job = get_object_or_404(Job, id=id, user=request.user)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            form = JobForm(instance=job)
            messages.success(request, "Job listing updated successfully.")
            return render(request, 'job/user/job_edit.html', {'form': form, 'job': job})
    else:
        form = JobForm(instance=job)

    return render(request, 'job/user/job_edit.html', {'form': form, 'job': job})

