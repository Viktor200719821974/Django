# Generated by Django 3.2.8 on 2021-10-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]