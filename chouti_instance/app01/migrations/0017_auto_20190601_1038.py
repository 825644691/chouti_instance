# Generated by Django 2.2.1 on 2019-06-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20190529_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chouti',
            name='praise_count',
            field=models.IntegerField(max_length=32),
        ),
    ]
