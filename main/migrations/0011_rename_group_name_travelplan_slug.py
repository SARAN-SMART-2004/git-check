# Generated by Django 5.0.6 on 2024-07-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_travelplan_group_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelplan',
            old_name='group_name',
            new_name='slug',
        ),
    ]