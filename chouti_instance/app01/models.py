from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32, db_index=True)
    email = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    ctime = models.DateTimeField(auto_created=True)
    secondname = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=4, null=True)
    signature = models.CharField(max_length=64, null=True)
    img = models.CharField(max_length=64)

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


class Chouti(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=32, null=True)
    praise_count = models.IntegerField(null=True, default=0)
    username = models.CharField(max_length=32)
    count = models.CharField(max_length=32, default=0)
    region = models.CharField(max_length=32, null=True)
    status = models.CharField(max_length=6, default=True)
    # 参数related_name="n"用作反向查询,

class Favor(models.Model):
    Chouti = models.ForeignKey("Chouti", on_delete=models.CASCADE)
    User = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    is_favor = models.CharField(max_length=32)



class Comment(models.Model):
    news = models.ForeignKey("Chouti", on_delete=models.CASCADE)
    user = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    ctime = models.DateTimeField(auto_now=True)
    device = models.CharField(max_length=16, null=True)
    parent_comment = models.ForeignKey("self", null=True, related_name="pc", on_delete=models.CASCADE)

