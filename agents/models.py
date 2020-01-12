from django.db import models
from django.contrib.auth.models import User,AbstractUser

from django.db.models.signals import post_save
import uuid
# Create your models here.

class AgentProfile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=40 , default='')
    phone = models.IntegerField(default=0)








    def __str__(self):
        return "{0} {1} {2}".format(self.user.username,self.user.first_name, self.user.last_name)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = AgentProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)