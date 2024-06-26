# Generated by Django 4.2.11 on 2024-05-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BoxData",
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
                ("box_code", models.TextField(max_length=15)),
                ("latitude", models.TextField(null=True)),
                ("longitude", models.TextField()),
                ("latitude2", models.TextField()),
                ("longitude2", models.TextField()),
                ("length", models.IntegerField()),
                ("width", models.IntegerField()),
                ("height", models.IntegerField()),
                ("sequence", models.IntegerField()),
                ("loadsequence", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("box_code", models.TextField(primary_key=True, serialize=False)),
                ("delivery_man_code", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("road_address", models.TextField(max_length=100)),
                ("detail_address", models.TextField(max_length=100)),
                ("phone", models.TextField(max_length=5)),
                ("date", models.DateField()),
            ],
        ),
    ]
