from django.contrib import messages
from django.contrib.auth import get_backends, login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from apps.job.models import Job
from common.utils.metadata import make_metadata

from .forms import (
    AccountProfile,
    EmployerProfileForm,
    EmployerSignupForm,
    TalentProfileForm,
    TalentSignupForm,
)
from .models import Employer, Talent


def get_backend_name():
    backend = get_backends()[0]
    return f"{backend.__module__}.{backend.__class__.__name__}"


def talent_view(request, id):
    """View function for talent single page."""
    talent = get_object_or_404(Talent, id=id)

    title_talent = talent.title or "Talent"

    title_first_name = f"{talent.first_name}" if talent.first_name else ""
    title_last_name = f"{talent.last_name}" if talent.last_name else ""
    title_space = " " if talent.first_name and talent.last_name else ""
    title_comma = " - " if talent.first_name or talent.last_name else ""

    metadata = make_metadata(
        request,
        {
            "title": f"{title_first_name}{title_space}{title_last_name}{title_comma}{title_talent}",
            "meta": {
                "description": "Remote Forge is a platform that connects remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs, Remote Talents",
                "robots": "index, follow",
            },
        },
    )

    data = {
        "talent": talent,
        "metadata": metadata,
    }

    return render(request, "user/talent.html", data)


def talents_view(request):
    """View function for talents list."""
    talents = Talent.objects.filter(is_published=True)

    metadata = make_metadata(
        request,
        {
            "title": f"Best Talent for Remote Jobs",
            "meta": {
                "description": "Remote Forge is a platform that connects remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs, Remote Talents",
                "robots": "index, follow",
            },
        },
    )

    data = {
        "talents": talents,
        "metadata": metadata,
    }

    return render(request, "user/talents.html", data)


def employer_view(request, id):
    """View function for employer single page."""
    employer = get_object_or_404(Employer, id=id)
    jobs = Job.objects.filter(user=employer.user, is_published=True)
    return render(request, "user/employer.html", {"employer": employer, "jobs": jobs})


def employers_view(request):
    """View function for employers list."""
    employers = Employer.objects.filter(is_published=True)
    return render(request, "user/employers.html", {"employers": employers})


def talent_signup_view(request):
    """View function for talent signup."""
    if request.method == "POST":
        form = TalentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            backend = get_backend_name()
            login(request, user, backend=backend)
            request.session["user_type"] = "talent"
            messages.success(
                request, "Registration successful! Welcome to our platform."
            )
            return redirect(reverse("welcome"))
    else:
        form = TalentSignupForm()
    return render(
        request,
        "allauth/account/signup_talent.html",
        {"form": form},
    )


def employer_signup_view(request):
    """View function for employer signup."""
    if request.method == "POST":
        form = EmployerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            backend = get_backend_name()
            login(request, user, backend=backend)
            request.session["user_type"] = "employer"
            messages.success(
                request, "Registration successful! Welcome to our platform."
            )
            return redirect(reverse("welcome"))
    else:
        form = EmployerSignupForm()

    login_url = reverse("account_login")

    return render(
        request,
        "allauth/account/signup_employer.html",
        {"form": form, "login_url": login_url},
    )


@login_required
def welcome_view(request):
    user_type = request.user.user_type
    if user_type not in ["talent", "employer"]:
        raise Http404
    return render(request, "./user/admin/welcome.html", {"user_type": user_type})


@login_required
def profile_view(request):

    if request.user.user_type == "talent":
        profile = get_object_or_404(Talent, user=request.user)
        form_class = TalentProfileForm
    elif request.user.user_type == "employer":
        profile = get_object_or_404(Employer, user=request.user)
        form_class = EmployerProfileForm
    else:
        raise Http404

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            request, "user/admin/profile.html", {"form": form, "profile": profile}
    else:
        form = form_class(instance=profile)

    return render(
        request, "user/admin/profile.html", {"form": form, "profile": profile}
    )


@login_required
def account_view(request):
    if request.method == "POST":
        form = AccountProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully.")
            return render(request, "user/admin/account.html", {"form": form})
    else:
        form = AccountProfile(instance=request.user)
    return render(request, "user/admin/account.html", {"form": form})
