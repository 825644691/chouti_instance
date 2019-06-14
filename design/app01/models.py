from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    usertype = models.ForeignKey("UserType", on_delete=models.CASCADE)
    evil = models.ManyToManyField("Evil")

class UserType(models.Model):
    type = models.CharField(max_length=12)


class Evil(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
