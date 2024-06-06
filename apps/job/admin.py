from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "city", "is_published", "created_at")


admin.site.register(Job, JobAdmin)
