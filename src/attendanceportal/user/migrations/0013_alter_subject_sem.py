# Generated by Django 4.2.7 on 2023-11-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0012_alter_attendance_student_roll_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
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
