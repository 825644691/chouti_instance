# Generated by Django 2.2.1 on 2019-05-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20190523_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='chouti',
            name='favor',
            field=models.CharField(max_length=32, null=True),
        ),
    ]