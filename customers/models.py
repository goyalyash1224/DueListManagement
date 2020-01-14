from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Customer(models.Model):
    """A typical class defining a model, derived from the Model class."""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others'),
    )

    Marital_status = (
        ('unmarried', 'Unmarried'),
        ('Married', 'Married')

    )


    # Fields
    id = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=30, help_text='Enter field documentation')
    father_husband_name =  models.CharField(max_length=30,default='', help_text='Enter field documentation')
    gender =  models.CharField(max_length= 1,default='M',choices=GENDER_CHOICES,help_text='Enter field documentation')
    hometown =  models.CharField(max_length= 20,default="", help_text='Enter field documentation')
    pincode =  models.CharField(help_text='Enter pincode',default = "", max_length=6)
    occupation =  models.CharField(max_length= 20,default='', help_text='Enter field documentation')
    date_joined = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(blank=True,help_text="Upload image")
    address = models.TextField(blank=True,default="")
    pan_number = models.IntegerField(default=0)
    pan_card_picture = models.ImageField(null=True, blank=True, help_text="Upload image")
    adhar_number = models.IntegerField(unique=True,default=0)
    adhar_card_pictures = models.ImageField(null=True, blank=True, help_text="Upload image")
    mob_no1 = models.IntegerField(default=0)
    mob_no2 = models.IntegerField(blank=True,null=True)
    dob = models.DateField()
    signature_image = models.ImageField(null=True, blank=True, help_text="Upload image")
    marital_status = models.CharField(max_length=9,default="Married", choices=Marital_status)

    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)



    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "{0}".format(self.name)




class Document(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    file = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
