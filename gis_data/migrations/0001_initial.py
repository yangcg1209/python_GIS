# Generated by Django 3.2.5 on 2021-07-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityAirQualityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='城市名')),
                ('date', models.CharField(max_length=10, null=True, verbose_name='日期')),
            ],
        ),
    ]
