# Generated by Django 3.1 on 2021-01-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0002_auto_20210119_2304"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="book",
        ),
        migrations.AddField(
            model_name="book",
            name="notes",
            field=models.ManyToManyField(to="study.Note"),
        ),
    ]
