# Generated by Django 4.2.11 on 2024-05-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Load', '0003_rename_loadseuqence_loadedboxdata_loadsequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadedboxdata',
            name='layerColor',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
    ]
