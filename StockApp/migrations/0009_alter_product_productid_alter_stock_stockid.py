# Generated by Django 4.2.6 on 2023-10-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0008_alter_customer_customerid_alter_product_productid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productId',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stockId',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
