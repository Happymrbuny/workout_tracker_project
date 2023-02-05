from datetime import date

from django.db import models

# Create your models here.
class Workout(models.Model):
    title = models.CharField(max_length=70, blank=False, default="")
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    timestamp = models.DateField(auto_now_add=True)
    musclegroup = models.CharField(max_length=70, blank=False, default="")

    def __str__(self):
        return self.title

