from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
