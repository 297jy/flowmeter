# Generated by Django 2.2 on 2020-02-23 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0028_auto_20200223_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dturegion',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowmeter.User', unique=True),
        ),
    ]
