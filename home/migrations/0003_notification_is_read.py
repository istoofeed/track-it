# Generated by Django 4.2.5 on 2023-12-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
    ]
