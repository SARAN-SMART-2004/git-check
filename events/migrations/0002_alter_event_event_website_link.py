# Generated by Django 5.0.6 on 2024-07-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_website_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
