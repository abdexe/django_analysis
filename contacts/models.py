from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.email