# Generated by Django 3.0 on 2021-02-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_index_lang_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='bg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
