# Generated by Django 2.2.1 on 2019-06-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0028_auto_20190602_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='chouti',
            name='region',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='chouti',
            name='count',
            field=models.CharField(default=0, max_length=32),
        ),
        migrations.AlterField(
            model_name='chouti',
            name='praise_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
