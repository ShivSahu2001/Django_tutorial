# Generated by Django 4.2.1 on 2023-06-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Receipe",
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
                ("receipeName", models.CharField(max_length=100)),
                ("receipeDescription", models.TextField()),
                ("receipeImage", models.ImageField(upload_to="receipe")),
            ],
        ),
    ]