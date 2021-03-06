# Generated by Django 3.0 on 2019-12-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=20)),
                ('album_title', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=1000)),
                ('song_numbers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(upload_to='songs/')),
                ('image', models.ImageField(upload_to='images/')),
                ('song_title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=120)),
                ('song_time', models.IntegerField()),
                ('release_date', models.DateField()),
                ('is_favorite', models.BooleanField(default=False)),
                ('genre', models.CharField(max_length=20)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
