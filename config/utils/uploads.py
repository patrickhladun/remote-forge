import os
from datetime import datetime


def get_uploads_path(instance, filename, path, filename_prefix):
    """
    Generate a file upload path with a unique filename.

    The filename is created using the user's email (with '@' and '.' replaced),
    a timestamp, and the original file extension.

    Args:
        instance (Model instance): The instance of the model containing the
        file.
        filename (str): The original filename.
        path (str): The directory path where the file will be saved.
        filename_prefix (str): The prefix to use for the new filename.

    Returns:
        str: The generated file path.
    """
    user_email = instance.user.email.replace("@", "-at-").replace(".", "-dot-")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{filename_prefix}-{user_email}-{timestamp}"
    f"{os.path.splitext(filename)[1]}"
    return os.path.join(path, new_filename)
