# Generated by Django 5.0 on 2023-12-22 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('shipping_address', models.CharField(max_length=255)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_postal_code', models.CharField(blank=True, max_length=12, null=True)),
                ('shipping_area', models.CharField(blank=True, max_length=50, null=True)),
                ('order_status', models.CharField(default='pending', max_length=50)),
                ('shipping_courier', models.CharField(max_length=50)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]