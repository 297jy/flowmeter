# Generated by Django 3.0.2 on 2020-03-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0033_remove_meter_valve'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='label',
            field=models.CharField(default='', max_length=128),
        ),
    ]