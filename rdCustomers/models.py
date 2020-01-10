from django.db import models
from datetime import  date
import uuid

from customers.models import *

# Create your models here.


class RdUser(models.Model):
    Status_Choices = (
        ('Active','Active'),
        ('Inactive', 'Inactive')
    )

    id = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    customer = models.OneToOneField('customers.Customer',on_delete=models.CASCADE,related_name='rd_user')
    # status = models.CharField(default="Inactive",choices=Status_Choices, max_length=10)
    serial_no = models.CharField(max_length=4,unique=True)
    # account_no = models.IntegerField()
    # cif_id = models.IntegerField()
    Denom_value = models.PositiveIntegerField()
    start_date = models.DateField()
    # end_date = models.DateField()
    total_policy_year = models.PositiveIntegerField()
    # family_group  = models.BooleanField()
    # family_name = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank = True, null = True,related_name='families')
    # villager = models.BooleanField()
    # belongToOtherCity = models.BooleanField()
    # local = models.BooleanField()
    # Market_user = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "{0} - {1}".format(self.customer.name, self.serial_no)

        # Metadata

    class Meta:
        ordering = ['serial_no']


# class Family(models.Model):
#     name_family = models.OneToOneField(Costumer,on_delete=models.CASCADE)
#
#
#     # Metadata
#     class Meta:
#         ordering = ['-name_family']
#
#     # Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of MyModelName."""
#         return reverse('family-view', args=[str(self.id)])
#
#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#
#         return "{0} {1}".format(self.name_family, self.name_family.mob_no1)


import datetime
# YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
#
# year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

class RdData(models.Model):
    # YEAR_CHOICES = [(r, r) for r in range(rd_user_data.start_date.year, rd_user_data.end_date.year)]

    # def get_start_year(self):
    #     return datetime.date.self.start_date.year.value
    #
    #
    # def get_end_year(self):
    #     return self.rd_user_data.self.end_date.year.value





    # YEAR_CHOICES = [(r, r) for r in range(2013, 2020)]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rd_user = models.ForeignKey(RdUser, on_delete=models.CASCADE, related_name='rd_data')
    kisht_date = models.DateField(verbose_name='Kishat Month')
    payment_date = models.DateField(verbose_name="Payment Received date")
    entry_time = models.DateTimeField(auto_now=True, null=True)
    message = models.TextField(max_length=250, blank=True,default='')



    def __str__(self):
        return "{0} ----  {1} ---- {2}-kishat           ".format(self.rd_user.customer.name,self.payment_date,self.kisht_date.strftime("%B"))


    def get_absolute_url(self):
        return reverse('rd_detail',args=[str(self.id)])




    class Meta:
        indexes = [models.Index(fields=['kisht_date'])]
        ordering =  ['kisht_date']
        verbose_name = 'rd-data'
        verbose_name_plural = 'RD data'
        constraints = [
            models.UniqueConstraint(fields=['rd_user', 'kisht_date'], name='unique kishat')
        ]





class Item(models.Model):
    PARTIAL_YEAR='%Y'
    PARTIAL_MONTH='%Y-%m'
    PARTIAL_DAY='%Y-%m-%d'
    PARTIAL_CHOICES = (
      (PARTIAL_YEAR, 'Year'),
      (PARTIAL_MONTH, 'Month'),
      (PARTIAL_DAY, 'Day'),
    )
    partial_date_part = models.CharField('Date part',
                                          choices=PARTIAL_CHOICES,
                                          max_length=10, )
    partial_date_date = models.DateField()
    some_comment = models.CharField('Comment', max_length=100, )

    def save(self, *args, **kwargs):
        if self.partial_date_part==self.PARTIAL_YEAR:
            self.partial_date_date = date( self.partial_date_date.year, 1, 1 )
        elif self.partial_date_part==self.PARTIAL_MONTH:
            self.partial_date_date = date( self.partial_date_date.year,
                                          self.partial_date_date.month, 1 )
        super(Item, self).save(*args, **kwargs)
