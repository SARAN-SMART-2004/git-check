# Generated by Django 5.0.6 on 2024-07-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/'),
        ),
        migrations.AddField(
            model_name='message',
            name='location',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
