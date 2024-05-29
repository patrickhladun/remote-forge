from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Job
from apps.user.models import Employer
from .forms import JobForm


def job(request, id):
    """View function for job."""
    job_obj = get_object_or_404(Job, id=id)
    employer = get_object_or_404(Employer, user=job_obj.user)
    jobs = Job.objects.filter(user=job_obj.user, is_published=True)

    return render(request, "job/job.html", {
        "job": job_obj,
        "employer": employer,
        "jobs": jobs
    })


def job_list(request):
    """View function for jobs."""
    city = request.GET.get('city')
    jobs = Job.objects.filter(is_published=True)
    data = []
    
    for job in jobs:
        employer = get_object_or_404(Employer, user=job.user)
        if city:
            if employer.city.lower() == city.lower():
                data.append({
                    'job': job,
                    'employer': employer
                })
        else:
            data.append({
                'job': job,
                'employer': employer
            })
    
    return render(request, "job/job_list.html", {"data": data})


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


@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully.')
        return redirect('user-job-list')
    return render(request, 'job/user/job_delete_confirm.html', {'job': job})