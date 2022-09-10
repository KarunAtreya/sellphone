
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'phoneimages/{filename}'.format(filename= filename)


class Phone(models.Model):

    Brand=(
        ('A', 'Apple'),
        ('S', 'Samsung'),
    )

    Phone_Model =(
        ('7', 'Iphone 7'),
        ('8', 'Iphone 8'),
        ('X', 'Iphone X'),
        ('11', 'Iphone 11'),
        ('12', 'Iphone 12'),
        ('13', 'Iphone 13'),
    )

    Phone_Variant = (
        ('B', 'Base'),
        ('Pl', 'Plus'),
        ('Pr', 'Pro'),
        ('Prm', 'Promax'),
    )

    Battery_Health = (
        ('A', 'Above 90%'),
        ('B', '80% to 90%'),
        ('C', 'Below 90%'),
    )

    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.CharField(choices=Brand, max_length=25)
    model = models.CharField(choices=Phone_Model, max_length=25)
    variant =models.CharField(choices=Phone_Variant, max_length=25)
    storage = models.IntegerField()
    battery = models.CharField(choices=Battery_Health, max_length=25)
    touchorfaceid = models.CharField(max_length=25)
    truetone=models.BooleanField(default=True)
    screen_issues = models.BooleanField(default=False)
    body_issues= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} :{self.owner.username}    ({self.created_on})'

class PhoneInfo(models.Model):
    phone = models.OneToOneField(
        Phone,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.TextField()
    color = models.CharField(max_length=20, null=True)
    image = models.ImageField(_("Image"), upload_to = upload_to, default= "phoneimages/default.jpg")
    price = models.FloatField(null=True)
    negotiable = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.phone.id}:{self.phone.owner}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    location = models.CharField(max_length=25)
    profile_pic = models.ImageField(_("Image"), upload_to = upload_to, default= "profileimages/profiledefault.jpg")

    def __str__(self):
        return f'{self.user}'

    