# Generated by Django 3.1.7 on 2021-05-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210522_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
