# Generated by Django 5.2 on 2025-04-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='api_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
