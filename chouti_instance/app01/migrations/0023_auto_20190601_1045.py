# Generated by Django 2.2.1 on 2019-06-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0022_auto_20190601_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chouti',
            name='title',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]