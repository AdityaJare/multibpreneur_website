# Generated by Django 5.2.1 on 2025-05-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinquiry',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactinquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactinquiry',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
