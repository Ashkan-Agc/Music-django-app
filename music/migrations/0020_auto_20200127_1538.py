# Generated by Django 3.0.2 on 2020-01-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_auto_20200127_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='profile/'),
        ),
    ]
