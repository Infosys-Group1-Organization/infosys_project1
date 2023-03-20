# Generated by Django 4.1.5 on 2023-01-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="import_data1",
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
                ("title", models.CharField(max_length=70)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10000)),
                ("summary", models.TextField(default="This is my first django app..")),
            ],
        ),
    ]
