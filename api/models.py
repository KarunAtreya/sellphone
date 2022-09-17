
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_elasticsearch_dsl_drf.wrappers import dict_to_obj


def upload_to(instance, filename):
    return 'phoneimages/{filename}'.format(filename= filename)


class Phone(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    storage = models.IntegerField() 
    color = models.CharField(max_length=20)
    battery = models.CharField(max_length=25)
    screen_size = models.CharField(max_length=25)
    camera = models.CharField(max_length=25)
    description = models.TextField()
    price = models.FloatField(null=True)
    negotiable = models.BooleanField(null=False)
    image1 = models.ImageField(_("Image"), upload_to = upload_to, default= "phoneimages/default.jpg")
    image2 = models.ImageField(_("Image"), upload_to = upload_to, default= "phoneimages/default.jpg")
    image3 = models.ImageField(_("Image"), upload_to = upload_to, default= "phoneimages/default.jpg")
    image4 = models.ImageField(_("Image"), upload_to = upload_to, default= "phoneimages/default.jpg")
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} : {self.brand} {self.model} Posted by {self.user.username}'
    
    class Meta:
        ordering = ['id']

    @property
    def user_indexing(self):
        wrapper = dict_to_obj({
            'id': self.user.id,
            'username': self.user.username,
        })

        return wrapper



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    location = models.CharField(max_length=25)
    profile_pic = models.ImageField(_("Image"), upload_to = upload_to, default= "profileimages/profiledefault.jpg")

    def __str__(self):
        return f'{self.user} profile info'
