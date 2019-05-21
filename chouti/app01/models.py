from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)


class Place(models.Model):
    place = models.CharField(max_length=64)