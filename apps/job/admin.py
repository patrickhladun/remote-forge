from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Job model.

    Attributes:
        list_display (tuple): A list of field names to display in the admin
        list view.
    """

    list_display = ("user", "title", "city", "is_published", "created_at")


admin.site.register(Job, JobAdmin)
