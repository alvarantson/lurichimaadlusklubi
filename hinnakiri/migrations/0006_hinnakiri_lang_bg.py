# Generated by Django 2.2.9 on 2021-02-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hinnakiri', '0005_hinnakiri_lang_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='hinnakiri_lang',
            name='bg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]