from django.contrib import admin
from .models import Phone, PhoneInfo, UserProfile
# Register your models here.

admin.site.register(Phone)
admin.site.register(PhoneInfo)
admin.site.register(UserProfile)
