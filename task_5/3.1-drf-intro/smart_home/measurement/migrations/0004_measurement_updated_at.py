# Generated by Django 4.2.4 on 2023-08-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_remove_measurement_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
