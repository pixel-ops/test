# Generated by Django 4.2 on 2023-05-08 06:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quiz",
            name="Quiz_type",
        ),
    ]
