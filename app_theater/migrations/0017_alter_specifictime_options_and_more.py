# Generated by Django 5.0.6 on 2024-06-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_theater', '0016_alter_specifictime_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specifictime',
            options={'ordering': ['hour_minute', 'id']},
        ),
        migrations.AlterField(
            model_name='specifictime',
            name='hour_minute',
            field=models.TimeField(),
        ),
    ]
