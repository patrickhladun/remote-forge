from django.utils.text import slugify

from apps.user.models import Employer, Talent


def page_slug(request):
    """
    Generate a slug based on the request path for use in templates.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing the page slug.
    """
    path = request.path.strip("/").replace("/", "-")
    slug = slugify(path) if path else "home"
    return {"page_slug": slug}


def site_data(request):
    """
    Provide site-wide data to be used in templates, including user profile
    image.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing site name and user profile image if
        authenticated.
    """
    profile = None

    if request.user.is_authenticated:
        profile = {"image": None}
        try:
            talent_profile = Talent.objects.get(user=request.user)
            profile["image"] = talent_profile.image
        except Talent.DoesNotExist:
            try:
                employer_profile = Employer.objects.get(user=request.user)
                profile["image"] = employer_profile.image
            except Employer.DoesNotExist:
                profile["image"] = None

    data = {"site_name": "Remote Forge", "profile": profile}
    return data
