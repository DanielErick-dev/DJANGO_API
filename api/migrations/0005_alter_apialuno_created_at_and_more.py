# Generated by Django 5.0.6 on 2024-07-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_apialuno_expiration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apialuno",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="apialuno",
            name="expiration_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
