from django.db import models

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   # last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   # comment = models.CharField(max_length=1000)
   reservation_date = models.DateField(null=True)
   reservation_slot = models.SmallIntegerField(default=10)

   def __str__(self):
      return self.first_name
   


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField(max_length=1000, default='')
   def __str__(self):
      return self.name
      
