# Generated by Django 2.2.9 on 2021-02-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pood', '0003_auto_20210204_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='pood_lang',
            name='title',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
