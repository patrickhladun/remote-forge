from django import template
from django.utils.safestring import mark_safe
import os

register = template.Library()

@register.simple_tag
def icon(name, size='md'):
    sizes = {
        'sm': 'icon--sm',
        'md': 'icon--md',
        'lg': 'icon--lg',
    }
    
    size = sizes.get(size, 'icon--md')  # Default to 'md' if size is not found

    try:
        with open(os.path.join('static/assets/icons', f'{name}.svg')) as f:
            icon = f.read()
            return mark_safe(f'<div class="icon {size} text-center">{icon}</div>')
    except FileNotFoundError:
        return mark_safe('<!-- Icon not found -->')