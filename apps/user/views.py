from django.contrib.auth import login, get_backends
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Talent, Employer
from apps.job.models import Job
from .forms import AccountProfile, TalentProfileForm, EmployerProfileForm, TalentSignupForm, EmployerSignupForm


def get_backend_name():
    # Get the backend and return its dotted import path string
    backend = get_backends()[0]
    return f"{backend.__module__}.{backend.__class__.__name__}"

def talent_view(request, id):
    """View function for talent single page."""
    talent = get_object_or_404(Talent, id=id)
    return render(request, "user/talent.html", {"talent": talent})


def talents_view(request):
    """View function for talents list."""
    talents = Talent.objects.filter(is_published=True)
    return render(request, 'user/talents.html', {'talents': talents})


def employer_view(request, id):
    """View function for employer single page."""
    employer = get_object_or_404(Employer, id=id)
    jobs = Job.objects.filter(user=employer.user, is_published=True)
    return render(request, "user/employer.html", {"employer": employer, "jobs": jobs})


def employers_view(request):
    """View function for employers list."""
    employers = Employer.objects.filter(is_published=True)
    return render(request, 'user/employers.html', {'employers': employers})


def talent_signup_view(request):
    """View function for talent signup."""
    if request.method == 'POST':
        form = TalentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            backend = get_backend_name()
            login(request, user, backend=backend)
            return redirect(reverse('profile'))
    else:
        form = TalentSignupForm()
    return render(request, 'allauth/account/signup_talent.html', {'form': form})


def employer_signup_view(request):
    """View function for employer signup."""
    if request.method == 'POST':
        form = EmployerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            backend = get_backend_name()
            login(request, user, backend=backend)
            return redirect(reverse('profile'))
    else:
        form = EmployerSignupForm()
    return render(request, 'allauth/account/signup_employer.html', {'form': form})


@login_required
def profile_view(request):
    
    if request.user.user_type == "talent":
        profile = get_object_or_404(Talent, user=request.user)
        form_class = TalentProfileForm
    elif request.user.user_type == "employer":
        profile = get_object_or_404(Employer, user=request.user)
        form_class = EmployerProfileForm
    else:
        return redirect("error")  # Redirect or handle the error

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = form_class(instance=profile)

    return render(request, 'user/admin/profile.html', {"form": form})

@login_required
def account_view(request):
    if request.method == "POST":
        form = AccountProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully.")
            return redirect("account")
    else:
        form = AccountProfile(instance=request.user)
    return render(request, 'user/admin/account.html', {"form": form})