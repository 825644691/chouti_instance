from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.IntegerField()


class Student(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    cls = models.ForeignKey("Classes", on_delete=models.CASCADE)





class Classes(models.Model):
    caption = models.CharField(max_length=64)
    teacher = models.ManyToManyField("Teacher")


class Teacher(models.Model):
    name = models.CharField(max_length=64)


class File(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=128)