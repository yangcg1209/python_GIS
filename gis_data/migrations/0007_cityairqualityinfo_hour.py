# Generated by Django 3.2.5 on 2021-07-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_data', '0006_alter_cityairqualityinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityairqualityinfo',
            name='hour',
            field=models.CharField(max_length=100, null=True, verbose_name='小时'),
        ),
    ]
