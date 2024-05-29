from django import forms
from apps.job.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "is_published",
            "title",
            "city",
            "salary",
            "schedule",
            "details",
            ]