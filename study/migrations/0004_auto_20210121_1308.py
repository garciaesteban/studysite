# Generated by Django 3.1 on 2021-01-21 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0003_auto_20210121_1251"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="notes",
        ),
        migrations.AddField(
            model_name="note",
            name="book",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="study.book",
            ),
            preserve_default=False,
        ),
    ]
