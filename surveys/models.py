from django.db import models
from datetime import datetime
from accounts.models import CustomUser

class Survey(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    comment = models.TextField(default='null')
    hear_brand = models.TextField(default='null')
    see_brand = models.TextField(default='null')
    speaking_brand = models.TextField(default='null')
    buy_before = models.CharField(max_length=200,default='null')
    use_before = models.CharField(max_length=200,default='null')
    rating_experience = models.IntegerField(default=0)
    rating_feedback = models.IntegerField(default=0)
    sharing_probabilite = models.IntegerField(default=0)
    other_brand  = models.CharField(max_length=200,default='null')
    best_brand = models.CharField(max_length=200,default='null')
    user_age = models.IntegerField(default=24)
    user_country = models.CharField(max_length=150,default='egypt', null=True, blank=True)
    user_city = models.CharField(max_length=150,default='city', null=True, blank=True)
    user_gender = models.CharField(max_length=150,default='Male', null=True, blank=True)
    sent_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment

    

class Surveyno(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    comment = models.TextField(default='null')
    looking = models.TextField(default='null')
    problems = models.TextField(default='null')
    products = models.TextField(default='null')
    speaking_brand = models.TextField(default='null')
    buy_before = models.CharField(max_length=200,default='null')
    rating_feedback = models.IntegerField(default=0)
    sharing_probabilite = models.IntegerField(default=0)
    user_age = models.IntegerField(default=24)
    user_country = models.CharField(max_length=150,default='egypt', null=True, blank=True)
    user_city = models.CharField(max_length=150,default='city', null=True, blank=True)
    user_gender = models.CharField(max_length=150,default='Male', null=True, blank=True)
    sent_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment