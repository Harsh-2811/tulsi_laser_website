# Generated by Django 3.2.8 on 2021-10-17 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211017_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]