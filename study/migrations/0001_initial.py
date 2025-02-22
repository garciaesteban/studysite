# Generated by Django 3.1 on 2021-01-20 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("chapter", models.PositiveIntegerField()),
                ("start_page", models.PositiveIntegerField()),
                ("end_page", models.PositiveIntegerField()),
                ("date_created", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(blank=True, max_length=255, null=True)),
                ("publisher", models.CharField(blank=True, max_length=255, null=True)),
                ("started_reading", models.DateField(auto_now_add=True)),
                ("finished_reading", models.DateField(blank=True, null=True)),
                ("chapters", models.PositiveIntegerField(default=0)),
                ("notes", models.ManyToManyField(to="study.Note")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
