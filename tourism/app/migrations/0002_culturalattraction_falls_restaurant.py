# Generated by Django 5.1.2 on 2024-12-17 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalAttraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('historical_significance', models.TextField(blank=True, null=True)),
                ('entrance_fee_adult', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('entrance_fee_discounted', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('phone', models.CharField(max_length=15)),
                ('gmail', models.CharField(max_length=30)),
                ('facebook', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cultural_attractions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Falls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('entrance_fee_adult', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('entrance_fee_discounted', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('phone', models.CharField(max_length=15)),
                ('gmail', models.CharField(max_length=30)),
                ('facebook', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='falls', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('cuisine_type', models.CharField(max_length=100)),
                ('price_range', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('gmail', models.CharField(max_length=30)),
                ('facebook', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='app/images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
