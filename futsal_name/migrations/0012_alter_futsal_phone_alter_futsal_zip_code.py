# Generated by Django 5.0 on 2024-01-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("futsal_name", "0011_remove_futsal_email_adress_futsal_email_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="futsal",
            name="phone",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="futsal",
            name="zip_code",
            field=models.CharField(max_length=250),
        ),
    ]