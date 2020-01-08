from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # class Meta:
    #     ordering = ('-self.user.first_name')

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
