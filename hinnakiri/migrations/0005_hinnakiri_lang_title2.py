# Generated by Django 2.2.9 on 2021-02-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hinnakiri', '0004_hinnakiri_lang_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='hinnakiri_lang',
            name='title2',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]