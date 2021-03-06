# Generated by Django 2.2 on 2020-02-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0024_meterstate_sensor_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meterstate',
            name='sensor_error_flag',
        ),
        migrations.AlterField(
            model_name='meterstate',
            name='battery_pressure_state',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='meterstate',
            name='recharge_state',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='meterstate',
            name='sensor_state',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='meterstate',
            name='valve_state',
            field=models.IntegerField(default=-1),
        ),
    ]
