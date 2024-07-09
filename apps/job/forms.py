from django import forms

from apps.job.models import Job


class JobForm(forms.ModelForm):
    """
    A form for creating and updating Job instances.

    Attributes:
        Meta (class): Contains metadata options for the JobForm.
            model (Job): The model that the form is associated with.
            fields (list): The fields to include in the form.
    """

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
    """
    A form for filtering job listings based on keyword and location.

    Attributes:
        keyword (CharField): The keyword to filter job listings by title
        (optional).
        location (CharField): The location to filter job listings by city or
        country (optional).
    """

    keyword = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
