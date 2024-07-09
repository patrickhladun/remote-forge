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
    """
    Retrieve the name of the authentication backend.

    Returns:
        str: The module and class name of the first authentication backend.
    """
    backend = get_backends()[0]
    return f"{backend.__module__}.{backend.__class__.__name__}"


def talent_view(request, id):
    """
    View function for displaying a talent profile page.

    Retrieves the talent with the given ID, constructs metadata for the page,
    and renders the talent profile template.

    Args:
        request (HttpRequest): The HTTP request object.
        id (UUID): The ID of the talent to display.

    Returns:
        HttpResponse: The rendered talent profile page.
    """

    talent = get_object_or_404(Talent, id=id)

    title_talent = talent.title or "Talent"

    title_first_name = f"{talent.first_name}" if talent.first_name else ""
    title_last_name = f"{talent.last_name}" if talent.last_name else ""
    title_space = " " if talent.first_name and talent.last_name else ""
    title_comma = " - " if talent.first_name or talent.last_name else ""

    metadata = make_metadata(
        request,
        {
            "title": f"{title_first_name}{title_space}{title_last_name}"
            f"{title_comma}{title_talent}",
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
        "talent": talent,
        "metadata": metadata,
    }

    return render(request, "user/talent.html", data)


def talents_view(request):
    """
    View function for displaying the talents listing page.

    Retrieves all published talents, constructs metadata for the page,
    and renders the talents listing template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered talents listing page.
    """
    talents = Talent.objects.filter(is_published=True)

    metadata = make_metadata(
        request,
        {
            "title": f"Best Talent for Remote Jobs",
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
        "talents": talents,
        "metadata": metadata,
    }

    return render(request, "user/talents.html", data)


def employer_view(request, id):
    """
    View function for displaying the employer's profile page.

    Retrieves the employer and their published jobs, constructs metadata
    for the page, and renders the employer profile template.

    Args:
        request (HttpRequest): The HTTP request object.
        id (str): The UUID of the employer.

    Returns:
        HttpResponse: The rendered employer profile page.
    """

    employer = get_object_or_404(Employer, id=id)
    jobs = Job.objects.filter(user=employer.user, is_published=True)

    title_employer = employer.company or "Employer"
    title_city = employer.city or ""
    title_country = employer.country or ""
    title_dash = " - " if employer.city or employer.country else ""
    title_comma = ", " if employer.city and employer.country else ""

    metadata = make_metadata(
        request,
        {
            "title": f"{title_employer}{title_dash}{title_city}{title_comma}"
            f"{title_country}",
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
        "employer": employer,
        "jobs": jobs,
        "metadata": metadata,
    }

    return render(request, "user/employer.html", data)


def employers_view(request):
    """
    View function for displaying a list of published employers.

    Retrieves all published employers, constructs metadata for the page, and
    renders the employers list template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered employers list page.
    """

    employers = Employer.objects.filter(is_published=True)

    metadata = make_metadata(
        request,
        {
            "title": f"Best Remote Employers",
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
        "employers": employers,
        "metadata": metadata,
    }

    return render(request, "user/employers.html", data)


def talent_signup_view(request):
    """
    View function for handling talent signup.

    Processes the talent signup form, logs in the new user if the form is
    valid, and redirects to the welcome page. If the form is not valid, it
    re-renders the signup form with errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered signup page or a redirect to the welcome
        page.
    """

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
    """
    View function for handling employer signup.

    Processes the employer signup form, logs in the new user if the form is
    valid, and redirects to the welcome page. If the form is not valid, it
    re-renders the signup form with errors. Also, provides a login URL for
    users who already have an account.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered signup page with form or a redirect to the
        welcome page.
    """

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
    """
    View function for the welcome page.

    Displays a welcome page based on the user's type (talent or employer).
    If the user type is not talent or employer, it raises a 404 error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered welcome page.
    """
    user_type = request.user.user_type
    if user_type not in ["talent", "employer"]:
        raise Http404
    return render(
        request, "./user/admin/welcome.html", {"user_type": user_type}
    )


@login_required
def profile_view(request):
    """
    View function for handling user profiles.

    Displays and processes the profile form for users based on their type
    (talent or employer). If the user type is not recognized, it raises a 404
    error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page with form or a redirect upon
        successful update.
    """

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
            request, "user/admin/profile.html", {
                "form": form,
                "profile": profile,
            }
    else:
        form = form_class(instance=profile)

    return render(
        request, "user/admin/profile.html", {"form": form, "profile": profile}
    )


@login_required
def account_view(request):
    """
    View function for handling user account details.

    Displays and processes the account profile form for users. If the form is
    submitted and valid, the user's account details are updated and a success
    message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered account page with form or the updated
        account page.
    """

    if request.method == "POST":
        form = AccountProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully.")
            return render(request, "user/admin/account.html", {"form": form})
    else:
        form = AccountProfile(instance=request.user)
    return render(request, "user/admin/account.html", {"form": form})
