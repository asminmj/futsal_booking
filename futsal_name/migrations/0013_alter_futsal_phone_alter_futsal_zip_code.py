# Generated by Django 5.0 on 2024-01-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("futsal_name", "0012_alter_futsal_phone_alter_futsal_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="futsal",
            name="phone",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="futsal",
            name="zip_code",
            field=models.CharField(max_length=10),
        ),
    ]