# Generated by Django 4.2.5 on 2023-12-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0002_users_lastpaid"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="applied_date",
            field=models.DateField(null=True),
        ),
    ]