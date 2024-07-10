from django.apps import AppConfig


class JobConfig(AppConfig):
    """
    Configuration class for the Job application.

    Attributes:
        default_auto_field (str): The type of primary key to use for models in
        this app.
        name (str): The full Python path to the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.job"
