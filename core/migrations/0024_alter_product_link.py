# Generated by Django 3.2.8 on 2021-10-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_product_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.SlugField(max_length=100),
        ),
    ]
