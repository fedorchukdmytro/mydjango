from django.db import models

# Create your models here.


class Group(models.Model):
    discipline = models.CharField(max_length=200)
    hours = models.IntegerField(default=30)
   
    
