from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Futsal(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=200)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField( max_length=10)

    def __str__(self):
        return self.name
    
class FutsalbookingUser(models.Model):
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.EmailField('User Email')
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + '' + self.last_name
  




# Create your models here.
class Futsalbookingdetail(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    booking_date = models.DateTimeField('Booking Date', default=timezone.now)
    location = models.CharField('Location', max_length=250)
    futsal  = models.ForeignKey(Futsal, null=True, blank=True, on_delete=models.CASCADE)
    incharge = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    phone = models.CharField('Phone', max_length=10)
    rate = models.IntegerField('Rate')
    players = models.ManyToManyField(FutsalbookingUser, blank=True)

    def __str__(self):
        return self.name




