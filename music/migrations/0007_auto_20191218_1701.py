# Generated by Django 2.2.7 on 2019-12-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_delete_pictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='song_numbers',
        ),
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_time',
        ),
    ]
