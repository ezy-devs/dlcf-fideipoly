# Generated by Django 5.1.6 on 2025-02-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
