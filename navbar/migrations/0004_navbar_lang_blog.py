# Generated by Django 3.0 on 2021-02-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0003_auto_20210204_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar_lang',
            name='blog',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
