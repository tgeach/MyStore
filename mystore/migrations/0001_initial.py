# Generated by Django 4.1.3 on 2022-12-13 23:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("unit", models.CharField(max_length=250)),
                ("price_per_unit", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                "verbose_name_plural": "Inventory",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("street_address", models.TextField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "province_state",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                ("zip_postal", models.CharField(blank=True, max_length=10, null=True)),
                ("country", models.CharField(blank=True, max_length=80, null=True)),
                (
                    "contact_phone",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mystore.account",
                    ),
                ),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mystore.inventory",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mystore.location",
                    ),
                ),
            ],
        ),
    ]
