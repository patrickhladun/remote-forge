from django.db import models
from apps.user.models import User
import uuid

# Create your models here.
class Job(models.Model):
    """Model definition for Talent."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=56, null=True, blank=True)
    salary = models.CharField(max_length=40, null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)
    details = models.JSONField(default=list, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'job_listing'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self) -> str:
        return self.title