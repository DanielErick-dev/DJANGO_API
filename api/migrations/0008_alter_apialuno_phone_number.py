# Generated by Django 5.0.6 on 2024-08-13 19:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_apialuno_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apialuno",
            name="phone_number",
            field=models.CharField(
                max_length=11,
                validators=[django.core.validators.MinLengthValidator(11)],
            ),
        ),
    ]
