# Generated by Django 4.1.5 on 2023-01-07 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdata',
            old_name='ticker',
            new_name='symbol',
        ),
    ]
