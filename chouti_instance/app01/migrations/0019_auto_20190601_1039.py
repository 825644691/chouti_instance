# Generated by Django 2.2.1 on 2019-06-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_auto_20190601_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chouti',
            name='praise_count',
            field=models.IntegerField(null=True),
        ),
    ]