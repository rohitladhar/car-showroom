from django.db import models

# Create your models here.
class Bookcar(models.Model):
    bycname= models.CharField(max_length=100)
    bycphone= models.CharField(max_length=15)
    bycmodel= models.CharField(max_length=20,default=None)
    bycemail= models.EmailField(max_length=100)
    bycadvance= models.IntegerField()
    bycdate= models.CharField(max_length=15)

class Business(models.Model):
    bname= models.CharField(max_length=100)
    bphone= models.CharField(max_length=15)
    boption= models.CharField(max_length=20,default=None)
    bmeets= models.DateField(max_length=20)
    bdesc= models.TextField()
    bemail= models.EmailField(max_length=50)

class Service(models.Model):
    objects = models.Manager()
    object=models.Manager()
    sname= models.CharField(max_length=100)
    sreg= models.CharField(max_length=15)
    sphone= models.CharField(max_length=15)
    semail= models.EmailField(max_length=100)
    sdate= models.CharField(max_length=20)
    sslot= models.CharField(max_length=20)

class Car(models.Model):
    objects = models.Manager()
    object=models.Manager()
    car_name=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    low_price=models.IntegerField()
    high_price=models.IntegerField()
    car_image=models.ImageField(upload_to='pics')

class Bookservice(models.Model):
    objects = models.Manager()
    object=models.Manager()
    date=models.CharField(max_length=20)
    mbooked=models.IntegerField(default=0)
    mavailable=models.IntegerField(default=10)
    ebooked=models.IntegerField(default=0)
    eavailable=models.IntegerField(default=10)