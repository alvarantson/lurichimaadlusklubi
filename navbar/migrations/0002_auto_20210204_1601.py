# Generated by Django 2.2.9 on 2021-02-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=999, unique=True),
        ),
    ]