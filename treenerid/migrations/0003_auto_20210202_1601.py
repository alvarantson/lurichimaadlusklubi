# Generated by Django 3.0.2 on 2021-02-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treenerid', '0002_treenerid_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treener',
            name='nimi',
            field=models.CharField(max_length=999),
        ),
    ]
