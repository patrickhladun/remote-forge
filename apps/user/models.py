# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Talent(models.Model):
    """Model definition for Talent."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.CharField(max_length=255)



class Company(models.Model):
    """Model definition for Company."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField()

