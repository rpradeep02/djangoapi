from django.db import models

# Create your models here.
class User(models.Model):
    no = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=20)
    tz = models.CharField(max_length=30)

class Activity(models.Model):
    no = models.CharField(max_length=9)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)