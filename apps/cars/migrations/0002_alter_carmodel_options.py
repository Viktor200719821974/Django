# Generated by Django 3.2.8 on 2021-10-28 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('id',), 'verbose_name': 'Машина', 'verbose_name_plural': 'Машина'},
        ),
    ]