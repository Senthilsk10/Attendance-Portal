# Generated by Django 4.2.7 on 2023-11-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0013_alter_subject_sem"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance_pool",
            name="datefield",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="attendance_pool",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="attendance_pool",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
    ]