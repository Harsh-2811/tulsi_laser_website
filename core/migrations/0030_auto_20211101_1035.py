# Generated by Django 3.2.6 on 2021-11-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_product_youtube_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='product',
            name='youtube_video_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]