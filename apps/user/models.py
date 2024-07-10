import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django_jsonform.models.fields import JSONField

from config.utils.uploads import get_uploads_path


def validate_resume_extension(value):
    """
    Validates the file extension of a resume upload.

    Ensures that the uploaded file has a valid extension.
    Supported extensions are: .pdf, .doc, .docx.

    Args:
        value (File): The uploaded file.

    Raises:
        ValidationError: If the file extension is not valid.
    """
    import os

    extension = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".doc", ".docx"]
    if not extension.lower() in valid_extensions:
        raise ValidationError(
            "Unsupported file extension. Allowed extensions are: .pdf, .doc, "
            ".docx"
        )


def talent_upload_profile_path(instance, filename):
    """
    Returns the upload path for a talent profile image.
    """
    return get_uploads_path(instance, filename, "talent/profile/", "profile")


def talent_upload_resume_path(instance, filename):
    """
    Returns the upload path for a talent resume.
    """
    return get_uploads_path(instance, filename, "talent/resumes/", "resume")


def employer_upload_profile_path(instance, filename):
    """
    Returns the upload path for an employer profile image.
    """
    return get_uploads_path(instance, filename, "employer/profile/", "profile")


SOCIAL_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "site": {
                "type": "string",
                "choices": [
                    "facebook",
                    "twitter",
                    "linkedin",
                    "instagram",
                    "github",
                    "dribbble",
                    "behance",
                    "youtube",
                    "pinterest",
                ],
            },
            "url": {"type": "string"},
        },
        "required": ["site", "url"],
    },
}

SKILLS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "string",
    },
}

EDUCATION_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "level": {"type": "string"},
            "status": {"type": "string"},
            "start_date": {"type": "string"},
            "end_date": {"type": "string"},
            "still_on": {"type": "boolean"},
        },
    },
}

EXPERIENCE_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "position": {"type": "string"},
            "company": {"type": "string"},
            "start_date": {"type": "string"},
            "end_date": {"type": "string"},
            "still_on": {"type": "boolean"},
            "responsibilities": {
                "type": "string",
                "widget": "textarea",
            },
        },
    },
}


class CustomUserManager(BaseUserManager):
    """
    Custom manager for handling user creation with email as the unique
    identifier.
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Internal method to create a user with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields for the user model.

        Raises:
            ValueError: If the email is not provided.

        Returns:
            User: The created user instance.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """
        Public method to create a regular user.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The created user instance.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Public method to create a superuser.

        Args:
            email (str): The email address of the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields for the user model.

        Raises:
            ValueError: If any of is_admin, is_staff, or is_superuser are not
            set to True.

        Returns:
            User: The created superuser instance.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Custom user model for handling user accounts with email as the unique
    identifier.

    Attributes:
        id (UUIDField): The unique identifier for the user.
        email (EmailField): The email address of the user.
        username (CharField): The username of the user.
        date_joined (DateTimeField): The date and time when the user joined.
        last_login (DateTimeField): The date and time of the user's last login.
        is_admin (BooleanField): Indicates if the user is an admin.
        is_active (BooleanField): Indicates if the user is active.
        is_staff (BooleanField): Indicates if the user is staff.
        is_superuser (BooleanField): Indicates if the user is a superuser.
        user_type (CharField): The type of user (e.g., talent, employer).
        objects (CustomUserManager): The custom manager for the user model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def has_perm(self, perm, obj=None):
        """
        Checks if the user has a specific permission.

        Args:
            perm (str): The permission to check.
            obj (Model): The object to check the permission against.

        Returns:
            bool: True if the user is an admin, otherwise False.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Checks if the user has permissions to view the app 'app_label'.

        Args:
            app_label (str): The app label to check.

        Returns:
            bool: Always True as all users have permissions to view any app.
        """
        return True

    def __str__(self):
        """
        Returns the string representation of the user.

        Returns:
            str: The username of the user.
        """
        return self.username


class Talent(models.Model):
    """
    Model definition for Talent.

    Represents a talent user profile with personal and professional details.

    Attributes:
        id (UUIDField): The unique identifier for the talent.
        user (OneToOneField): The associated user account.
        first_name (CharField): The first name of the talent.
        last_name (CharField): The last name of the talent.
        phone (CharField): The phone number of the talent.
        city (CharField): The city where the talent is located.
        country (CharField): The country where the talent is located.
        image (ImageField): The profile image of the talent.
        bio (TextField): A short biography of the talent.
        title (CharField): The professional title of the talent.
        resume (FileField): The resume of the talent.
        website (URLField): The personal or professional website of the talent.
        social (JSONField): Social media links of the talent.
        experience (JSONField): Professional experience of the talent.
        education (JSONField): Educational background of the talent.
        interests (CharField): Interests of the talent.
        skills (JSONField): Skills of the talent.
        created_at (DateTimeField): The date and time when the talent profile
        was created.
        updated_at (DateTimeField): The date and time when the talent profile
        was last updated.
        is_published (BooleanField): Indicates whether the talent profile is
        published.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=30, blank=True, default="")
    phone = models.CharField(max_length=30, blank=True, default="")
    city = models.CharField(max_length=75, blank=True, default="")
    country = models.CharField(max_length=56, blank=True, default="")
    image = models.ImageField(
        upload_to=talent_upload_profile_path,
        null=True,
        blank=True,
    )
    bio = models.TextField(blank=True, default="")
    title = models.CharField(max_length=100, blank=True, default="")
    resume = models.FileField(
        upload_to=talent_upload_resume_path,
        null=True,
        blank=True,
        validators=[validate_resume_extension],
    )
    website = models.URLField(max_length=200, blank=True, default="")
    social = JSONField(schema=SOCIAL_SCHEMA, null=True, blank=True)
    experience = JSONField(schema=EXPERIENCE_SCHEMA, null=True, blank=True)
    education = JSONField(schema=EDUCATION_SCHEMA, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    skills = JSONField(schema=SKILLS_SCHEMA, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Talent"
        verbose_name_plural = "Talents"

    def __str__(self) -> str:
        """
        Returns the string representation of the talent profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username


class Employer(models.Model):
    """
    Model definition for Employer.

    Represents an employer user profile with personal and company details.

    Attributes:
        id (UUIDField): The unique identifier for the employer.
        user (OneToOneField): The associated user account.
        first_name (CharField): The first name of the employer.
        last_name (CharField): The last name of the employer.
        email (EmailField): The email address of the employer.
        phone (CharField): The phone number of the employer.
        company (CharField): The name of the employer's company.
        about (TextField): A description of the employer or company.
        image (ImageField): The profile image of the employer.
        website (URLField): The website of the employer's company.
        city (CharField): The city where the employer is located.
        country (CharField): The country where the employer is located.
        social (JSONField): Social media links of the employer.
        created_at (DateTimeField): The date and time when the employer
        profile was created.
        updated_at (DateTimeField): The date and time when the employer
        profile was last updated.
        is_published (BooleanField): Indicates whether the employer profile is
        published.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=30, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=30, blank=True, default="")
    company = models.CharField(max_length=100, blank=True, default="")
    about = models.TextField(blank=True, default="")
    image = models.ImageField(
        upload_to=employer_upload_profile_path, null=True, blank=True
    )
    website = models.URLField(max_length=200, blank=True, default="")
    city = models.CharField(max_length=75, blank=True, default="")
    country = models.CharField(max_length=56, blank=True, default="")
    social = JSONField(schema=SOCIAL_SCHEMA, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"

    def __str__(self) -> str:
        """
        Returns the string representation of the employer profile.

        Returns:
            str: The username of the associated user and the company name.
        """
        return f"{self.user.username} {self.company}"
