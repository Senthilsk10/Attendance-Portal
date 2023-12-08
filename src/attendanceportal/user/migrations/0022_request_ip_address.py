# Generated by Django 4.2.7 on 2023-12-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_attendance_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.0'),
            preserve_default=False,
        ),
    ]