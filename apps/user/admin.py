from django.contrib import admin
from .models import User, Talent, Employer

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
          


admin.site.register(User, UserAdmin)
admin.site.register(Talent)
admin.site.register(Employer)
