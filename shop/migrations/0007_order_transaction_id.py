# Generated by Django 5.0.6 on 2024-06-22 21:30

import shop.models
import uuid
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_remove_order_transaction_id_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="transaction_id",
            field=shop.models.ShortUUIDField(
                default=uuid.uuid4, editable=False, unique=True
            ),
        ),
    ]
