# Generated by Django 5.1.6 on 2025-02-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
