# Generated by Django 5.0 on 2023-12-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("futsal_name", "0008_rename_booking_detail_futsalbookingdetail_futsal"),
    ]

    operations = [
        migrations.AddField(
            model_name="futsalbookingdetail",
            name="name",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]