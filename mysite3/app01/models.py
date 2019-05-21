from django.db import models


# Create your models here.
class Book2Author(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    author = models.ForeignKey("author", on_delete=models.CASCADE)
    #差一个联合唯一

    class Meta:
        unique_together = ["author", "book"]


class Publish(models.Model):
    my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.city


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# class AuthorDetail(models.Model):
#     sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),))
#     email = models.EmailField()
#     addres = models.CharField(max_length=50)
#     birthday = models.DateField()
#     author = models.OneToOneField("Author")
#
#     def __str__(self):
#         return self.author


class Book(models.Model):
    title = models.CharField(max_length=64, verbose_name="书名")
    price = models.IntegerField(max_length=64)
    color = models.CharField(max_length=64, editable=True)
    page_num = models.IntegerField(max_length=64)
    publisher = models.ForeignKey("Publish", on_delete=models.CASCADE)#一对多关系--》ForeignKey，书是多，所以外键在书里面

    #接受对象
    author = models.ManyToManyField("Author")

    def __str__(self):
        return self.title
