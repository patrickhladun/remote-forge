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
            "content": {
                "type": "string",
                "widget": "textarea",
            },
        },
        "required": ["heading", "content"],
    },
}


class Job(models.Model):
    """
    Represents a job listing.

    Attributes:
        id (UUIDField): The unique identifier for the job, generated
        automatically.
        user (ForeignKey): The user who posted the job, linked to the User
        model.
        title (CharField): The title of the job.
        city (CharField): The city where the job is located (optional).
        country (CharField): The country where the job is located (optional).
        salary (CharField): The salary for the job (optional).
        schedule (CharField): The schedule details for the job (optional).
        details (JSONField): Additional details about the job in JSON format
        (optional).
        created_at (DateTimeField): The date and time when the job was created.
        updated_at (DateTimeField): The date and time when the job was last
        updated.
        is_published (BooleanField): Indicates whether the job is published or
        not.

    Meta:
        db_table (str): The name of the database table.
        verbose_name (str): The singular name for the model.
        verbose_name_plural (str): The plural name for the model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, related_name="jobs", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=56, blank=True, default="")
    country = models.CharField(max_length=56, blank=True, default="")
    salary = models.CharField(max_length=40, blank=True, default="")
    schedule = models.CharField(max_length=100, blank=True, default="")
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
