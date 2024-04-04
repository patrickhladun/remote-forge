from django.contrib import admin
from .models import User, Talent, Employer

# Register your models here.
admin.site.register(User)
admin.site.register(Talent)
admin.site.register(Employer)
