from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialisation = models.CharField(max_length=200)
    
