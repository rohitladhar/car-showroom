from django.db import models


class Variant(models.Model):

    name = models.CharField(max_length=30)
    cmodel=models.CharField(max_length=30)
    cprice=models.CharField(max_length=30)
    

class Newcustomer(models.Model):
    objects = models.Manager()
    object=models.Manager()
    cname=models.CharField(max_length=50)
    cmodel=models.CharField(max_length=50)
    cvarinat=models.CharField(max_length=50)
    cengine=models.CharField(max_length=30)
    cphone=models.FloatField()
    cshow=models.CharField(max_length=30)
    cunique=models.CharField(max_length=30)
    ctax=models.FloatField()
    cemail=models.EmailField(max_length=50)
    cprice=models.FloatField()
    cadvance=models.FloatField()
    cmode=models.CharField(max_length=30)
    cemi=models.CharField(max_length=30)
    cloan=models.FloatField()
    

class Newservice(models.Model):
    objects = models.Manager()
    object=models.Manager()
    sname= models.CharField(max_length=100)
    sphone= models.FloatField()
    semail= models.EmailField(max_length=50)
    sdate= models.CharField(max_length=50)
    sprice= models.FloatField()
    sacc= models.CharField(max_length=100)
    stax= models.FloatField()
    stotal=models.FloatField()
    sunique=models.CharField(max_length=50)
    sdiscount=models.FloatField()
    sacctotal= models.FloatField()
    

class Accessories(models.Model):
    objects = models.Manager()
    object=models.Manager()
    name= models.CharField(max_length=50)
    price=models.IntegerField()

class NewShowroom(models.Model):
    objects = models.Manager()
    object=models.Manager()
    smonth= models.CharField(max_length=20)
    syear= models.CharField(max_length=20)
    srent= models.FloatField()
    sshow= models.CharField(max_length=50)
    smain= models.FloatField()
    sunits= models.FloatField()
    stotal= models.FloatField()
    

    