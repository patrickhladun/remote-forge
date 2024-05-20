from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_jsonform.models.fields import JSONField
import uuid

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to allow email login and creation of users with the `hide_email` field.
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Create a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    user_type = models.CharField(max_length=10)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # For checking permissions. to keep it simple all admin have ALL permissons    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username

class Talent(models.Model):
    """Model definition for Talent."""
    
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
                "responsibilities": {"type": "textarea"},
            },
        },
    }
    
    SOCIAL_SCHEMA = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "social": {
                    "type": "string",
                    "choices": ["facebook", "twitter", "linkedin", "instagram", "github", "dribbble", "behance", "youtube", "pinterest"],
                },
                "url": {"type": "string"},
            },
        },
    }

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=75, null=True, blank=True)
    country = models.CharField(max_length=56, null=True, blank=True)
    image = models.ImageField(upload_to='media/talent/profile/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    resume = models.FileField(upload_to='media/talent/resumes/', null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    social = JSONField(schema=SOCIAL_SCHEMA, null=True, blank=True)
    experience = JSONField(schema=EXPERIENCE_SCHEMA, null=True, blank=True)
    education = JSONField(schema=EDUCATION_SCHEMA, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_published = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Talent'
        verbose_name_plural = 'Talents'

    def __str__(self) -> str:
        return self.user.username


class Employer(models.Model):
    """Model definition for Employer."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="media/employer/profile/", null=True, blank=True
    )
    website = models.URLField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=75, null=True, blank=True)
    country = models.CharField(max_length=56, null=True, blank=True)
    social = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"

    def __str__(self) -> str:
        return f"{self.user.username} {self.company}"

