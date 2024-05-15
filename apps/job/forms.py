from django import forms
from apps.job.models import Listing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["is_published","title", "city", "salary", "schedule", "details", "skills"]