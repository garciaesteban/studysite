# Generated by Django 3.1 on 2021-02-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0006_auto_20210127_2037"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="note",
            options={"ordering": ["-date_created"]},
        ),
    ]
