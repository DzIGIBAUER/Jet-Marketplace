# Generated by Django 5.0.1 on 2024-02-01 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('cabin_height', models.FloatField(verbose_name='Cabin Height')),
                ('cabin_width', models.FloatField(verbose_name='Cabin Width')),
                ('cabin_length', models.FloatField(verbose_name='Cabin Length')),
                ('luggage_volume', models.FloatField(verbose_name='Luggage Volume')),
                ('max_persons', models.IntegerField(verbose_name='Max persons')),
                ('range', models.IntegerField(verbose_name='Range')),
                ('speed', models.IntegerField(verbose_name='Speed')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planes.category')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planes.producer')),
            ],
        ),
    ]
