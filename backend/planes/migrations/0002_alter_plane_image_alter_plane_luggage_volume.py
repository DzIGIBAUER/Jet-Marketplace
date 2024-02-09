# Generated by Django 5.0.1 on 2024-02-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='image',
            field=models.ImageField(upload_to='plane', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='plane',
            name='luggage_volume',
            field=models.FloatField(null=True, verbose_name='Luggage Volume'),
        ),
    ]
