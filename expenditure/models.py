from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse,get_object_or_404
abcstring = RegexValidator(r'^[A-Za-z ]*$', 'Only characters are allowed.')

# Create your models here.

class EmployeeDetail(models.Model):
    objects = models.Manager()
    object=models.Manager()
    npost= models.CharField(max_length=20)
    nname= models.CharField(max_length=50, validators=[abcstring])
    nphone=models.FloatField()
    nemail=models.EmailField(max_length=50)
    nid=models.CharField(max_length=20)
    noffice=models.CharField(max_length=50)
    ndate=models.CharField(max_length=50)
    npass=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('employee-record', kwargs={
            'pk': self.pk
        })

class Record(models.Model):
    objects = models.Manager()
    object=models.Manager()
    rpost= models.CharField(max_length=20)
    rname= models.CharField(max_length=50)
    rid=models.CharField(max_length=20)
    roffice=models.CharField(max_length=50)
    rmonth=models.CharField(max_length=50)
    ryear=models.CharField(max_length=50)
    rpay=models.FloatField()
    rhour=models.FloatField()
    rover=models.FloatField()
    rhoursum=models.FloatField()
    roversum=models.FloatField()
    rleave=models.FloatField()
    rabsent=models.FloatField()
    rfoul=models.FloatField()
    rallow=models.FloatField()
    rtotal=models.FloatField()

class Position(models.Model):
    objects = models.Manager()
    object=models.Manager()
    post=models.CharField(max_length=50)
    pay=models.FloatField()

class Application(models.Model):
    objects = models.Manager()
    object=models.Manager()
    empid= models.CharField(max_length=50)
    date= models.CharField(max_length=50)
    desc= models.CharField(max_length=2000)
    status=models.CharField(max_length=30)
    reason=models.CharField(max_length=50)

