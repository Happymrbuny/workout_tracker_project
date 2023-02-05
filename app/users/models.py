from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    email = models.CharField(max_length=65, blank=False, default='')
    