# Generated by Django 5.0.6 on 2024-06-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_alter_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="transaction_id",
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
