# Generated by Django 4.2.4 on 2023-08-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(),
        ),
    ]
