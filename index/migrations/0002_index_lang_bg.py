# Generated by Django 2.2.9 on 2021-02-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='bg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
