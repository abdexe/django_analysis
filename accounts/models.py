from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField()
    gender = models.CharField(max_length=150,default='Male', null=True, blank=True)
    city = models.CharField(max_length=150,default='cairo', null=True, blank=True)
    country = models.CharField(max_length=150,default='Egypt', null=True, blank=True)
