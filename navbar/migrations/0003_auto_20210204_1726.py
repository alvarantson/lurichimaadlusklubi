# Generated by Django 3.0 on 2021-02-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0002_auto_20210204_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar_lang',
            name='hinnakiri',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='navbar_lang',
            name='meist',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='navbar_lang',
            name='pood',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='navbar_lang',
            name='treenerid',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='navbar_lang',
            name='tutvustus',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]