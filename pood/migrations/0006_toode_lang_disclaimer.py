# Generated by Django 2.2.9 on 2021-02-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pood', '0005_toode_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='toode_lang',
            name='disclaimer',
            field=models.TextField(blank=True),
        ),
    ]