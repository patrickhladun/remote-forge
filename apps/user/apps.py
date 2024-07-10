from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Django AppConfig for the User application.

    This class configures the User application, setting the default
    auto field type and the application name.

    Attributes:
        default_auto_field (str): Specifies the type of primary key field to
        use for models.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"
