# Generated by Django 3.0.2 on 2020-02-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0007_navigationbar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='remark',
            field=models.CharField(default='', max_length=256),
        ),
    ]