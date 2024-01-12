# Generated by Django 5.0.1 on 2024-01-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_remove_flightpacket_request_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="carrier",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="flight",
            name="arrival_time_stamp",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_time_stamp",
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name="Carrier",
        ),
    ]
