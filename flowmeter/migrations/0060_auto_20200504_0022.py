# Generated by Django 3.0.2 on 2020-05-04 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0059_auto_20200504_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='unexecutedopr',
            name='meter_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='waitopr',
            name='meter_id',
            field=models.IntegerField(default=0),
        ),
    ]