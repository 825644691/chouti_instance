# Generated by Django 2.2.1 on 2019-05-23 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chouti',
            name='favor',
        ),
    ]
