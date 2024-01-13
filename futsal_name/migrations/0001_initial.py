# Generated by Django 5.0 on 2023-12-31 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Futsal_name",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Futsal Name")),
                ("address", models.CharField(max_length=200, verbose_name="Address")),
                ("zip_code", models.CharField(max_length=10, verbose_name="Zip Code")),
                (
                    "phone",
                    models.CharField(max_length=10, verbose_name="Contact Phone"),
                ),
                ("web", models.URLField(blank=True, verbose_name="WebSite Adress")),
                (
                    "email_adress",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FutsalbookingUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, verbose_name="User Email")),
                ("phone", models.CharField(max_length=10, verbose_name="User Phone")),
            ],
        ),
        migrations.CreateModel(
            name="Futsalbookingdetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("booking_date", models.DateTimeField(verbose_name="Booking Date")),
                ("location", models.CharField(max_length=250, verbose_name="Location")),
                ("incharge", models.CharField(max_length=200, verbose_name="Incharge")),
                ("phone", models.CharField(max_length=10, verbose_name="Phone")),
                ("rate", models.IntegerField(max_length=5, verbose_name="Rate")),
                (
                    "futsal_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="futsal_name.futsal_name",
                    ),
                ),
                (
                    "players",
                    models.ManyToManyField(
                        blank=True, to="futsal_name.futsalbookinguser"
                    ),
                ),
            ],
        ),
    ]
