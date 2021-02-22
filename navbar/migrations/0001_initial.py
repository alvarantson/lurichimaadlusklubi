# Generated by Django 3.0.2 on 2021-02-01 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50, unique=True)),
                ('gmaps_x', models.CharField(max_length=10, unique=True)),
                ('gmaps_y', models.CharField(max_length=10, unique=True)),
                ('gmaps_zoom', models.CharField(max_length=2, unique=True)),
                ('gmaps_API', models.CharField(max_length=64, unique=True)),
                ('open_hours', models.CharField(blank=True, max_length=64, unique=True)),
                ('footer_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=3, unique=True)),
                ('flag', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=999)),
                ('icon', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(blank=True, max_length=15)),
                ('logo', models.ImageField(upload_to='')),
                ('lang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
    ]
