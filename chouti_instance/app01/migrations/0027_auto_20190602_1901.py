# Generated by Django 2.2.1 on 2019-06-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_auto_20190601_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='img',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='secondname',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='signature',
            field=models.CharField(max_length=64, null=True),
        ),
    ]