# Generated by Django 4.2.11 on 2024-03-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Box", "0002_delivery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="height",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="length",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="width",
            field=models.IntegerField(),
        ),
    ]
