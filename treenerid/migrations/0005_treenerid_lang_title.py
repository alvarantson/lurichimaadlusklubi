# Generated by Django 3.0.2 on 2021-02-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treenerid', '0004_treener_pilt'),
    ]

    operations = [
        migrations.AddField(
            model_name='treenerid_lang',
            name='title',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]