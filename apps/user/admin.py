from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Employer, Talent, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "username")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TalentAdmin(admin.ModelAdmin):
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
        return mark_safe('<img src="%s" width="28" />' % obj.image.url)

    image_display.allow_tags = True
    image_display.short_description = "Image"

    def talent(self, obj):
        url = reverse(
            "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
            args=[obj.id],
        )
        return mark_safe('<a href="{}">{}</a>'.format(url, obj.title))


class EmployerAdmin(admin.ModelAdmin):
    list_display = ("image", "user", "company", "is_published", "created_at")
    search_fields = ("first_name",)

    def image_display(self, obj):
        return mark_safe('<img src="%s" width="28" />' % obj.image.url)

    image_display.allow_tags = True
    image_display.short_description = "Image"


admin.site.register(User, UserAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Employer, EmployerAdmin)
