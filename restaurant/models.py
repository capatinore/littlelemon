from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='') 


   def __str__(self):
      return self.name
   
class UserComments(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   comment = models.CharField(max_length=1000)
   
class Menu2(models.Model):
   item_name = models.CharField(max_length=200)
   category = models.CharField(max_length=200)
   description = models.CharField(max_length=1000)
   
class Bookings(models.Model):
   first_name = models.CharField(max_length=200)
   reservation_date = models.DateField()
   reservation_slot = models.SmallIntegerField(default=10)

   def __str__(self): 
      return self.first_name