# Generated by Django 3.0 on 2021-02-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_index_lang_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='liitu_meiega',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='lurchist',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='meist',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
