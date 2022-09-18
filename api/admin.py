from django.contrib import admin
from .models import Phone, UserProfile
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):

    """ Phone Admin"""

    list_display = ('id','brand', 'model', 'price', 'negotiable','user')
    search_fields = ('brand',)


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):

    """User Admin"""
    list_display = ('user', 'phone_number','location','profile_pic')
    search_fields = ('user.name',)

