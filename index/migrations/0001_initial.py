# Generated by Django 2.2.9 on 2021-02-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('navbar', '0002_auto_20210204_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
    ]