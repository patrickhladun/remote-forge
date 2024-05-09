from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import User, Talent, Employer

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
          

class TalentAdmin(admin.ModelAdmin):
    list_display = ('image_display', 'talent', 'user', 'first_name','last_name', 'is_published', 'created_at')
    search_fields = ('fname',)
    
    def image_display(self, obj):
        return mark_safe('<img src="%s" width="28" />' % obj.image.url)
    
    image_display.allow_tags = True
    image_display.short_description = 'Image'
    
    def first_name(self, obj):
        return obj.fname

    def last_name(self, obj):
        return obj.lname
    
    def talent(self, obj):
        url = reverse("admin:%s_%s_change" % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
        return mark_safe('<a href="{}">{}</a>'.format(url, obj.title))
    
    

admin.site.register(User, UserAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Employer)
