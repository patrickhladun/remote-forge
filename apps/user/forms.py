
from django import forms
from .models import Talent


class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = [
            "is_published",
            "fname",
            "lname",
            "phone",
            "city",
            "country",
            "bio",
            "title",
            "resume",
            "experience",
            "education",
            "skills",
            "interests",
            "website",
            "social",
        ]
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "phone": "Phone",
            "city": "City",
            "country": "Country",
            "bio": "Bio",
            "title": "Title",
            "resume": "Resume",
            "experience": "Experience",
            "education": "Education",
            "skills": "Skills",
            "interests": "Interests",
            "website": "Website",
            "social": "Social",
            "is_published": "Published",
        }
        bio = forms.Textarea()
        is_published = forms.BooleanField()
        fname = forms.CharField(max_length=30)
        lname = forms.CharField(max_length=30)
        phone = forms.CharField(max_length=30)
        city = forms.CharField(max_length=75)
        country = forms.CharField(max_length=56)
        title = forms.CharField(max_length=100)
        resume = forms.FileField()
        experience = forms.JSONField()
        education = forms.JSONField()
        skills = forms.JSONField()
        interests = forms.CharField(max_length=255)
        website = forms.URLField(max_length=200)
        social = forms.JSONField()
        
        
class AccountProfile(forms.ModelForm):
    pass