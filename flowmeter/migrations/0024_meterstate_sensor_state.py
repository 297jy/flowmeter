# Generated by Django 2.2 on 2020-02-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0023_auto_20200221_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterstate',
            name='sensor_state',
            field=models.CharField(default='known', max_length=8),
        ),
    ]