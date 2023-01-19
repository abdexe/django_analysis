from django.db import models

class Companie(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        