# Generated by Django 4.1.5 on 2023-01-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.TextField(null=True)),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]
