from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse

from apps.user.models import Talent
from common.utils.metadata import make_metadata

from .forms import ContactForm, JobSearchForm


def home(request):
    talents = Talent.objects.filter(is_published=True)[:6]
    form = JobSearchForm()

    metadata = make_metadata(
        request,
        {
            "title": "Home | Find Your Perfect Remote Job",
            "meta": {
                "description": "Remote Forge is a platform that connects remote talents with remote jobs.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs, Remote Talents",
                "robots": "index, follow",
            },
        },
    )

    if request.GET:
        form = JobSearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            location = form.cleaned_data["location"]
            query_string = "?"
            if keyword:
                query_string += f"keyword={keyword}&"
            if location:
                query_string += f"location={location}&"
            return redirect(reverse("job-list") + query_string)

    data = {
        "talents": talents,
        "form": form,
        "metadata": metadata,
    }

    return render(request, "base/home.html", data)


def about(request):
    talents = Talent.objects.filter(is_published=True)[:6]

    metadata = make_metadata(
        request,
        {
            "title": "About | Your Gateway to Remote Job Opportunities",
            "meta": {
                "description": "Learn more about Remote Forge, our mission, vision, and the team that makes it all happen. Discover why we're dedicated to providing the best remote job opportunities.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs",
                "robots": "index, follow",
            },
        },
    )

    data = {
        "talents": talents,
        "metadata": metadata,
    }

    return render(request, "base/about.html", data)


def contact(request):
    metadata = make_metadata(
        request,
        {
            "title": "Contact Us for Remote Job Inquiries",
            "meta": {
                "description": "Contact us for any questions or assistance. Our team is here to help. Reach out via email, phone, or use the contact form on this page.",
                "keywords": "Remote Work, Remote Jobs, Work from Home, Online Jobs",
                "robots": "index, follow",
            },
        },
    )

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("contact_success")

    else:
        form = ContactForm()

    data = {
        "form": form,
        "metadata": metadata,
    }

    return render(request, "base/contact.html", data)


def contact_success(request):
    metadata = make_metadata(
        request,
        {
            "title": "Contact Form Submission Success",
            "meta": {
                "description": "Thank you for reaching out! We have received your message and will get back to you soon.",
                "robots": "no-index, no-follow",
            },
        },
    )

    data = {"metadata": metadata}

    return render(request, "base/contact-success.html", data)


def privacy(request):
    metadata = make_metadata(
        request,
        {
            "title": "Privacy Policy | How Remote Forge Protects Your Data",
            "meta": {
                "description": "Read the Remote Forge Privacy Policy to learn how we protect your personal data and ensure your privacy.",
                "keywords": "privacy policy, data protection, personal information, user privacy, Remote Forge",
                "robots": "index, follow",
            },
        },
    )

    data = {"metadata": metadata}

    return render(request, "base/privacy.html", data)


def terms(request):
    metadata = make_metadata(
        request,
        {
            "title": "Terms and Conditions | Remote Forge User Agreement",
            "meta": {
                "description": "Review the Remote Forge Terms and Conditions to understand the rules and guidelines for using our services.",
                "keywords": "terms and conditions, user agreement, terms of service, legal, Remote Forge",
                "robots": "index, follow",
            },
        },
    )

    data = {"metadata": metadata}

    return render(request, "base/terms.html", data)
