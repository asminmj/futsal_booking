# Generated by Django 5.0 on 2023-12-31 13:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "futsal_name",
            "0005_alter_futsal_name_address_alter_futsal_name_name_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="futsalbookingdetail",
            old_name="name",
            new_name="futsal_name",
        ),
    ]