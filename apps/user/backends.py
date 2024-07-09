from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    """
    Custom authentication backend for case-insensitive username lookup.

    This backend allows users to log in with their username in a
    case-insensitive manner. It overrides the default authentication method to
    perform a case-insensitive lookup for the username.

    Methods:
        authenticate(request, username=None, password=None, **kwargs):
            Authenticates the user by case-insensitive username lookup and
            password verification.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate the user using case-insensitive username lookup.

        Args:
            request (HttpRequest): The HTTP request object.
            username (str): The username of the user attempting to
            authenticate.
            password (str): The password of the user attempting to
            authenticate.
            **kwargs: Additional keyword arguments.

        Returns:
            User: The authenticated user object if authentication is
            successful.
            None: If authentication fails.
        """
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = "{}__iexact".format(
                UserModel.USERNAME_FIELD
            )
            user = UserModel._default_manager.get(
                **{case_insensitive_username_field: username}
            )
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                return user
