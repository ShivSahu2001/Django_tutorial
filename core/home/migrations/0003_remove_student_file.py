# Generated by Django 4.2.1 on 2023-06-02 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_student_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="file",
        ),
    ]
