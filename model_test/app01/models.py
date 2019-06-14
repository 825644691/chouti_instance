from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=64)
    favor = models.ManyToManyField("User", through="Favor", through_fields=("news", "user"))


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=32)


class Favor(models.Model):
    news = models.ForeignKey("News", on_delete=models.CASCADE, related_name="n")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="u")


# 字段级别的
# 数字，字符串(带正则的字段email)
# 时间
# 文件
# 图片
# 关系(一对一，一对多，多对多)
