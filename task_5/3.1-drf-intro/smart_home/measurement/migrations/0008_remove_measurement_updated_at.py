# Generated by Django 4.2.4 on 2023-08-28 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='updated_at',
        ),
    ]
