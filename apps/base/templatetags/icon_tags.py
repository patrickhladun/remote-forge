import os

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def icon(name, size="md"):
    """
    Generates an HTML span element containing an SVG icon.

    This function reads an SVG file from the static assets/icons directory and
    embeds it within a span element. If the specified SVG file is not found,
    it returns an HTML comment indicating that the icon was not found.

    Args:
        name (str): The name of the icon file (without .svg extension).
        size (str, optional): The size of the icon ('sm', 'md', or 'lg').
        Defaults to 'md'.

    Returns:
        str: The HTML string for the icon or a comment if the icon is not
        found.
    """

    sizes = {
        "sm": "icon--sm",
        "md": "icon--md",
        "lg": "icon--lg",
    }

    size = sizes.get(size, "icon--md")

    try:
        with open(os.path.join("static/assets/icons", f"{name}.svg")) as f:
            icon = f.read()
            return mark_safe(
                f'<span class="icon {size} text-center">{icon}</span>'
            )
    except FileNotFoundError:
        return mark_safe("<!-- Icon not found -->")
