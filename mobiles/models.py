from django.db import models

# Create your models here.

class MobileList(models.Model):
    brand = models.CharField(max_length=25)
    price = models.IntegerField()
    color = models.CharField(max_length=25)
    ram = models.CharField(max_length=25)
    storage = models.CharField(max_length=25)