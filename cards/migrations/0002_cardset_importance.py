# Generated by Django 4.2 on 2023-04-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardset",
            name="importance",
            field=models.BooleanField(null=True),
        ),
    ]
