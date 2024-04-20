from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Talent, Company

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Assuming an attribute `is_company` to differentiate between users
        # This part needs adjustment based on your actual user differentiation logic
        if hasattr(instance, 'is_company') and instance.is_company:
            Company.objects.create(user=instance)
        else:
            Talent.objects.create(user=instance)
