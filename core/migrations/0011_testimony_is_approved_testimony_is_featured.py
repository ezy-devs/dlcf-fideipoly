# Generated by Django 5.1.6 on 2025-04-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_testimony_email_testimony_full_name_testimony_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimony',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
