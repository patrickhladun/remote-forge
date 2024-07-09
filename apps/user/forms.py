import re

from allauth.account.forms import SignupForm
from django import forms

from .models import Employer, Talent, User


class TalentSignupForm(SignupForm):
    """
    Form for signing up talent users.

    This form extends the default SignupForm and adds custom validation for
    usernames. It also creates a Talent profile associated with the user upon
    successful registration.

    Methods:
        save(request): Saves the user and creates an associated Talent profile.
        clean_username(): Validates the username field with custom criteria.
    """

    def save(self, request):
        """
        Save the user and create an associated Talent profile.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            User: The saved user instance.
        """
        user = super(TalentSignupForm, self).save(request)
        user.user_type = "talent"
        user.save()
        talent = Talent.objects.create(user=user)
        talent.save()
        return user

    def clean_username(self):
        """
        Validate the username field with custom criteria.

        Ensures the username is unique, has a length between 4 and 30
        characters, is alphanumeric, starts with a letter, and contains only
        letters, numbers, or underscores.

        Returns:
            str: The cleaned username.

        Raises:
            forms.ValidationError: If the username does not meet the criteria.
        """
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError(
                "Username must be at least 4 characters"
            )
        if len(username) > 30:
            raise forms.ValidationError(
                "Username must be at most 30 characters"
            )
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
    """
    Form for signing up employer users.

    This form extends the default SignupForm and adds custom validation for
    usernames. It also creates an Employer profile associated with the user
    upon successful registration.

    Methods:
        save(request): Saves the user and creates an associated Employer
        profile.
        clean_username(): Validates the username field with custom criteria.
    """

    def save(self, request):
        """
        Save the user and create an associated Employer profile.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            User: The saved user instance.
        """
        user = super(EmployerSignupForm, self).save(request)
        user.user_type = "employer"
        user.save()
        employer = Employer.objects.create(user=user)
        employer.save()
        return user

    def clean_username(self):
        """
        Validate the username field with custom criteria.

        Ensures the username is unique, has a length between 4 and 30
        characters, is alphanumeric, starts with a letter, and contains only
        letters, numbers, or underscores.

        Returns:
            str: The cleaned username.

        Raises:
            forms.ValidationError: If the username does not meet the criteria.
        """
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError(
                "Username must be at least 4 characters"
            )
        if len(username) > 30:
            raise forms.ValidationError(
                "Username must be at most 30 characters"
            )
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
    """
    Form for updating the profile of a Talent.

    This form allows the user to update various fields related to the Talent's
    profile, including personal information, contact details, professional
    experience, education, and skills.

    Fields:
        - is_published: Indicates if the profile is published.
        - image: Profile image of the talent.
        - first_name: First name of the talent.
        - last_name: Last name of the talent.
        - phone: Contact phone number.
        - city: City where the talent is located.
        - country: Country where the talent is located.
        - bio: Biography of the talent.
        - title: Professional title.
        - resume: Resume of the talent.
        - experience: Professional experience.
        - education: Educational background.
        - skills: List of skills.
        - interests: Interests of the talent.
        - website: Personal or professional website.
        - social: Social media links.
    """

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
        }


class EmployerProfileForm(forms.ModelForm):
    """
    Form for updating the profile of an Employer.

    This form allows the user to update various fields related to the
    Employer's profile, including personal information, company details, and
    contact information.

    Fields:
        - is_published: Indicates if the profile is published.
        - first_name: First name of the employer.
        - last_name: Last name of the employer.
        - email: Contact email address.
        - phone: Contact phone number.
        - company: Name of the company.
        - about: Description about the company.
        - image: Profile image of the employer.
        - website: Company or personal website.
        - city: City where the employer is located.
        - country: Country where the employer is located.
        - social: Social media links.
    """

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

    def clean_company(self):
        """
        Ensure that the company field is not empty.

        Raises:
            ValidationError: If the company field is empty.

        Returns:
            str: The cleaned company name.
        """
        company = self.cleaned_data.get("company")
        if not company:
            raise forms.ValidationError("Company field is required.")
        return company


class AccountProfile(forms.ModelForm):
    """
    Form for updating user account details.

    This form allows the user to update their username and email address.
    Various validation checks are included to ensure the username meets
    specific criteria.

    Fields:
        - username: The user's username.
        - email: The user's email address.
    """

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
        """
        Validate the username field.

        Checks for uniqueness, length constraints, and alphanumeric
        requirements. Ensures the username starts with a letter and does not
        contain special characters.

        Raises:
            ValidationError: If any validation checks fail.

        Returns:
            str: The cleaned username.
        """
        username = self.cleaned_data["username"]
        if (
            User.objects.filter(username=username)
            .exclude(id=self.instance.id)
            .exists()
        ):
            raise forms.ValidationError("Username already exists")
        if len(username) < 4:
            raise forms.ValidationError(
                "Username must be at least 4 characters"
            )
        if len(username) > 30:
            raise forms.ValidationError(
                "Username must be at most 30 characters"
            )
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric")
        if not username[0].isalpha():
            raise forms.ValidationError("Username must start with a letter")
        if not re.match("^[a-zA-Z0-9]*$", username):
            raise forms.ValidationError(
                "Username must contain only letters, numbers, or underscores"
            )
        return username
