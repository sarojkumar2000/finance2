# Generated by Django 4.2.5 on 2023-12-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0003_users_applied_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="interest_amount",
            field=models.IntegerField(default=0),
        ),
    ]
