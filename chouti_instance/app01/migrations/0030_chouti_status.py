# Generated by Django 2.2.1 on 2019-06-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0029_auto_20190609_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='chouti',
            name='status',
            field=models.CharField(default=True, max_length=6),
        ),
    ]
