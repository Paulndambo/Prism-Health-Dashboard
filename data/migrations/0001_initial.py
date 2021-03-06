# Generated by Django 3.1.7 on 2021-05-22 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('Nearest_city', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Service Providers',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.category')),
            ],
            options={
                'verbose_name_plural': 'Product Sub-Categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cost', models.FloatField(default=0)),
                ('service_image', models.ImageField(upload_to='services/images')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.provider')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.FloatField()),
                ('product_image', models.ImageField(upload_to='products/images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.category')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.provider')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('date_of_birth', models.DateTimeField()),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(default='Kenya', max_length=200)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.county')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.service')),
            ],
        ),
    ]
