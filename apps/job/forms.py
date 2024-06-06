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


class JobsFilterForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
