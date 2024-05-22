
from django import forms
from .models import User, Talent, Employer

class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = [
            "is_published",
            "first_name",
            "last_name",
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
            "first_name": "First Name",
            "last_name": "Last Name",
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
       
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = [
            "is_published",
            "first_name",
            "last_name",
            "email",
            "phone",
            "company",
            "about",
            "image",
            "website",
            "city",
            "country",
            "social",
        ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "phone": "Phone",
            "company": "Company",
            "about": "About",
            "image": "Image",
            "website": "Website",
            "city": "City",
            "country": "Country",
            "social": "Social",
        }
        
        
class AccountProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "hide_email",
            "email",
        ]
        labels = {
            "username": "Username",
            "hide_email": "Hide my Email",
            "email": "Email",
        }