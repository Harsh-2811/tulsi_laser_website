# Generated by Django 3.2.8 on 2021-10-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_why_us_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_team',
            name='designation',
            field=models.CharField(max_length=50),
        ),
    ]