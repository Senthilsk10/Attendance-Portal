# Generated by Django 4.2.7 on 2023-11-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0014_attendance_pool_datefield_attendance_pool_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance_pool",
            name="sem",
            field=models.IntegerField(
                choices=[
                    (1, "first semester"),
                    (2, "second semester"),
                    (3, "third semester"),
                    (4, "fourth semester"),
                    (5, "fifth semester"),
                    (6, "sixth semester"),
                    (7, "seventh semester"),
                    (8, "eigth semester"),
                ]
            ),
        ),
    ]
