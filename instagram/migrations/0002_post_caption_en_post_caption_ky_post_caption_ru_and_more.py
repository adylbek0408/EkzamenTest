# Generated by Django 5.0.6 on 2024-06-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_ky',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
