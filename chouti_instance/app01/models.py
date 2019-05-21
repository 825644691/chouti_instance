from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32, db_index=True)
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    ctime = models.DateTimeField(auto_created=True)

    class Meta:
        index_together = [
            ("username", 'password'),
        ]

        unique_together = [
            ("username", 'password'),
        ]


class SendMsg(models.Model):
    email = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=6)
    stime = models.DateTimeField()
    time = models.IntegerField()

