# Generated by Django 4.2.4 on 2023-08-21 20:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(2, "MALE"), (3, "FEMALE"), (5, "NONBINARY")]
                    ),
                ),
                (
                    "orientation",
                    models.IntegerField(
                        choices=[
                            (2, "M"),
                            (3, "F"),
                            (5, "NB"),
                            (6, "MF"),
                            (10, "MNB"),
                            (15, "FNB"),
                            (30, "MFNB"),
                        ]
                    ),
                ),
                ("country", models.CharField(default="USA", max_length=200)),
                ("birth", models.DateTimeField()),
                (
                    "age",
                    models.IntegerField(
                        default=18,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(18),
                        ],
                    ),
                ),
                (
                    "minAge",
                    models.IntegerField(
                        default=18,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(18),
                        ],
                    ),
                ),
                (
                    "maxAge",
                    models.IntegerField(
                        default=100,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(18),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Matchmaker",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("country", models.CharField(default="USA", max_length=200)),
            ],
        ),
    ]
