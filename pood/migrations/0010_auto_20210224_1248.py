# Generated by Django 3.0.2 on 2021-02-24 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0007_auto_20210223_1640'),
        ('pood', '0009_toode_lang_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toode',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang'),
        ),
    ]
