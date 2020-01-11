# Generated by Django 3.0.2 on 2020-01-10 18:14

from django.db import migrations, models
import django.db.models.deletion
import functools
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("django_base_shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConcreteCart",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cart_token",
                    models.CharField(
                        default=functools.partial(secrets.token_hex, *(32,), **{}),
                        editable=False,
                        max_length=64,
                        unique=True,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ConcreteCheckoutDetails",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=100)),
                ("customer_company", models.CharField(blank=True, max_length=100)),
                ("customer_email", models.EmailField(max_length=254)),
                ("customer_phone", models.CharField(max_length=100)),
                ("customer_coupon", models.CharField(blank=True, max_length=100)),
                ("billing_address_same_as_shipping", models.BooleanField(default=True)),
                ("_billing_name", models.CharField(blank=True, max_length=100)),
                ("_billing_company", models.CharField(blank=True, max_length=100)),
                (
                    "_billing_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="django_base_shop.Address",
                    ),
                ),
                (
                    "shipping_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="django_base_shop.Address",
                    ),
                ),
                (
                    "shipping_selection",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="django_base_shop.ShippingOption",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ConcreteOrder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_placed", models.DateTimeField(auto_now_add=True)),
                (
                    "order_token",
                    models.CharField(
                        default=functools.partial(secrets.token_hex, *(16,), **{}),
                        editable=False,
                        max_length=32,
                        unique=True,
                    ),
                ),
                ("subtotal_paid", models.DecimalField(decimal_places=2, max_digits=7)),
                ("shipping_paid", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "checkout_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="test_shop.ConcreteCheckoutDetails",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ConcreteProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "handle",
                    models.CharField(
                        help_text="Unique idenitfier used select specific product.",
                        max_length=200,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("available", models.BooleanField(default=True)),
                ("back_in_stock", models.DateField(blank=True, null=True)),
                (
                    "order_priority",
                    models.PositiveSmallIntegerField(
                        default=1000,
                        help_text="Hint on how the product should be displayed in lists.",
                    ),
                ),
            ],
            options={"ordering": ["-order_priority"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="ConcreteOrderItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("price_paid", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="items",
                        to="test_shop.ConcreteOrder",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="test_shop.ConcreteProduct",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ConcreteCartItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="test_shop.ConcreteCart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="test_shop.ConcreteProduct",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="concretecart",
            name="checkout_details",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="test_shop.ConcreteCheckoutDetails",
            ),
        ),
        migrations.AddIndex(
            model_name="concreteorder",
            index=models.Index(
                fields=["order_token"], name="test_shop_c_order_t_a4f74d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="concretecart",
            index=models.Index(
                fields=["cart_token"], name="test_shop_c_cart_to_82cccd_idx"
            ),
        ),
    ]
