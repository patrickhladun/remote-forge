import uuid

from django.db import models
from django_jsonform.models.fields import JSONField

from apps.user.models import User

DETAILS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "heading": {
                "type": "string",
                "choices": [
                    "Job Description",
                    "About the Job",
                    "Benefits",
                    "Responsibilities",
                    "Requirements",
                    "Why Us",
                    "About Us",
                ],
            },
            "content": {"type": "textarea"},
        },
    },
}


class Job(models.Model):
    """Model definition for Talent."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=56, null=True, blank=True)
    salary = models.CharField(max_length=40, null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)
    details = JSONField(schema=DETAILS_SCHEMA, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = "job_listing"
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self) -> str:
        return self.title
