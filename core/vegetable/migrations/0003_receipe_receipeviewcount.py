# Generated by Django 4.2.1 on 2023-06-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vegetable", "0002_receipe_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipe",
            name="receipeViewCount",
            field=models.IntegerField(default=1),
        ),
    ]