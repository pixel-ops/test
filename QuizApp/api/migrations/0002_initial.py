# Generated by Django 4.2 on 2023-05-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz",
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
                ("name", models.CharField(max_length=122)),
                ("total_question", models.IntegerField(default=10)),
                ("time", models.IntegerField(default=30)),
                ("subject", models.CharField(max_length=122)),
                ("difficulty", models.CharField(max_length=122)),
                ("Quiz_type", models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question", models.TextField()),
                ("total_options", models.IntegerField(default=4)),
                (
                    "correct_answer",
                    models.CharField(blank=True, max_length=122, null=True),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quiz_name",
                        to="api.quiz",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Option",
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
                ("option", models.CharField(max_length=122)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.question"
                    ),
                ),
            ],
        ),
    ]