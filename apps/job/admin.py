from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'city', 'is_published', 'created_at')
    


admin.site.register(Listing, ListingAdmin)