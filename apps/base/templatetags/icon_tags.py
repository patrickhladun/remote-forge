import os

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def icon(name, size="md"):
    sizes = {
        "sm": "icon--sm",
        "md": "icon--md",
        "lg": "icon--lg",
    }

    size = sizes.get(size, "icon--md")

    try:
        with open(os.path.join("static/assets/icons", f"{name}.svg")) as f:
            icon = f.read()
            return mark_safe(f'<span class="icon {size} text-center">{icon}</span>')
    except FileNotFoundError:
        return mark_safe("<!-- Icon not found -->")
