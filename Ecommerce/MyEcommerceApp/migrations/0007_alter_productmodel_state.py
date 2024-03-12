# Generated by Django 4.2.1 on 2024-02-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyEcommerceApp", "0006_productmodel_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="state",
            field=models.CharField(
                choices=[("PU", "PUBLICADO"), ("BR", "BORRADOR"), ("PR", "PRIVADO")],
                default="BR",
                max_length=2,
            ),
        ),
    ]
