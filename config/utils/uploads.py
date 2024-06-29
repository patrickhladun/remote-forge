import os
from datetime import datetime


def get_uploads_path(instance, filename, path, filename_prefix):
    user_email = instance.user.email.replace("@", "-at-").replace(".", "-dot-")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = (
        f"{filename_prefix}-{user_email}-{timestamp}{os.path.splitext(filename)[1]}"
    )
    return os.path.join(path, new_filename)
