# Generated by Django 2.2.7 on 2019-12-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20191203_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
