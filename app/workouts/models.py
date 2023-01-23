from django.db import models

# Create your models here.
class Workout(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()