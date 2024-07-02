import re

from allauth.account.forms import SignupForm
from django import forms

from .models import Employer, Talent, User


class TalentSignupForm(SignupForm):
    def save(self, request):
        user = super(TalentSignupForm, self).save(request)
        user.user_type = "talent"
        user.save()
        talent = Talent.objects.create(user=user)
        talent.save()
        return user

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters")
        if len(username) > 30:
            raise forms.ValidationError("Username must be at most 30 characters")
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric")
        if not username[0].isalpha():
            raise forms.ValidationError("Username must start with a letter")
        if not re.match("^[a-zA-Z0-9]*$", username):
            raise forms.ValidationError(
                "Username must contain only letters, numbers, or underscores"
            )
        return username


class EmployerSignupForm(SignupForm):
    def save(self, request):
        user = super(EmployerSignupForm, self).save(request)
        user.user_type = "employer"
        user.save()
        employer = Employer.objects.create(user=user)
        employer.save()
        return user

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters")
        if len(username) > 30:
            raise forms.ValidationError("Username must be at most 30 characters")
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric")
        if not username[0].isalpha():
            raise forms.ValidationError("Username must start with a letter")
        if not re.match("^[a-zA-Z0-9]*$", username):
            raise forms.ValidationError(
                "Username must contain only letters, numbers, or underscores"
            )
        return username


class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = [
            "is_published",
            "image",
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
            "is_published": "Published",
            "image": "Profile Image",
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
            "is_published": "Published",
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
            "email",
        ]
        labels = {
            "username": "Username",
            "email": "Email",
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters")
        if len(username) > 30:
            raise forms.ValidationError("Username must be at most 30 characters")
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric")
        if not username[0].isalpha():
            raise forms.ValidationError("Username must start with a letter")
        if not re.match("^[a-zA-Z0-9]*$", username):
            raise forms.ValidationError(
                "Username must contain only letters, numbers, or underscores"
            )
        return username
