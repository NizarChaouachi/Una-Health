# Generated by Django 5.2 on 2025-05-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("una_health_app", "0002_glucosetablelvels_alter_user_user_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="GlucoseTableLvels",
        ),
    ]
