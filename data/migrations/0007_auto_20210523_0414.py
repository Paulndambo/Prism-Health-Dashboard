# Generated by Django 3.1.7 on 2021-05-23 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20210523_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.customer'),
        ),
    ]
