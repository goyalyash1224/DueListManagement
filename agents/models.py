from django.db import models
from django.contrib.auth.models import User,AbstractUser

from django.db.models.signals import post_save
from datetime import datetime
import uuid
# Create your models here.

class AgentProfile(models.Model):

    gender_choices = (
        ('Male','male'),
        ('Female','female'),
        ('Others','others')
    )


    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,default='',blank=True)
    city = models.CharField(max_length=40 , default='',blank=True)
    phone = models.IntegerField(default=0, blank=True,null=True)
    dob = models.DateField(blank=True,default=datetime.now)
    gender = models.CharField(max_length=6,choices=gender_choices,default='Male')





    def __str__(self):
        return "{0} {1} {2}".format(self.user.username,self.user.first_name, self.user.last_name, self.phone)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = AgentProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)