# Generated by Django 3.2.8 on 2021-10-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211017_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='map_address_written',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
