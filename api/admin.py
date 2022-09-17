from django.contrib import admin
from .models import Phone, UserProfile
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):

    """ Phone Admin"""

    list_display = ('id','brand', 'model', 'price', 'negotiable','user')
    search_fields = ('brand',)



admin.site.register(UserProfile)
