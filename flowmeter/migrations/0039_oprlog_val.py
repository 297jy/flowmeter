# Generated by Django 3.0.2 on 2020-03-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowmeter', '0038_auto_20200314_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='oprlog',
            name='val',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
