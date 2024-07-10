from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Employer, Talent, User


class UserAdmin(admin.ModelAdmin):
    """
    Admin interface options for the User model.

    This class customizes the Django admin interface for the User model,
    specifying how the model fields are displayed, searched, and filtered.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to include in the admin search.
        readonly_fields (tuple): Fields to set as read-only in the admin
        interface.
        filter_horizontal (tuple): No horizontal filters for this model.
        list_filter (tuple): No list filters for this model.
        fieldsets (tuple): No fieldsets for this model.
    """

    list_display = (
        "email",
        "username",
        "user_type",
        "date_joined",
        "last_login",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "username")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TalentAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Talent model.

    This class customizes the Django admin interface for the Talent model,
    specifying how the model fields are displayed, searched, and filtered.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to include in the admin search.
    """

    list_display = (
        "image_display",
        "talent",
        "user",
        "first_name",
        "last_name",
        "is_published",
        "created_at",
    )
    search_fields = ("first_name",)

    def image_display(self, obj):
        """
        Displays the talent's profile image in the admin list view.

        Args:
            obj (Talent): The Talent instance.

        Returns:
            str: HTML string for the image tag.
        """
        if obj.image:
            return mark_safe('<img src="%s" width="28" />' % obj.image.url)
        else:
            default_image_url = "/static/assets/images/avatar.png"
            return mark_safe('<img src="%s" width="28" />' % default_image_url)

    image_display.allow_tags = True
    image_display.short_description = "Image"

    def talent(self, obj):
        """
        Creates a clickable link to the talent's admin change page.

        Args:
            obj (Talent): The Talent instance.

        Returns:
            str: HTML string for the link tag.
        """
        url = reverse(
            "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
            args=[obj.id],
        )
        return mark_safe('<a href="{}">{}</a>'.format(url, obj.title))


class EmployerAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Employer model.

    This class customizes the Django admin interface for the Employer model,
    specifying how the model fields are displayed, searched, and filtered.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to include in the admin search.
    """

    list_display = (
        "image_display",
        "user",
        "company",
        "is_published",
        "created_at",
    )
    search_fields = ("first_name",)

    def image_display(self, obj):
        """
        Displays the employer's profile image in the admin list view.

        Args:
            obj (Employer): The Employer instance.

        Returns:
            str: HTML string for the image tag.
        """
        if obj.image:
            return mark_safe('<img src="%s" width="28" />' % obj.image.url)
        else:
            default_image_url = "/static/assets/images/avatar.png"
            return mark_safe('<img src="%s" width="28" />' % default_image_url)

    image_display.allow_tags = True
    image_display.short_description = "Image"

    def employer(self, obj):
        """
        Creates a clickable link to the employer's admin change page.

        Args:
            obj (Employer): The Employer instance.

        Returns:
            str: HTML string for the link tag.
        """
        url = reverse(
            "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
            args=[obj.id],
        )
        return mark_safe('<a href="{}">{}</a>'.format(url, obj.title))


admin.site.register(User, UserAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Employer, EmployerAdmin)
