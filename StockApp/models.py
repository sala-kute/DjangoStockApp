from django.db import models

class Product(models.Model):
    productId = models.IntegerField(primary_key=True,auto_created=True)
    productName = models.CharField(max_length=20)
    price = models.FloatField()
    unit = models.CharField(max_length=5)
    code = models.CharField(max_length=5)

class Supplier(models.Model):
    supplierId = models.IntegerField(primary_key=True)
    supplierName = models.CharField(max_length=20)
    supplierTin = models.CharField(max_length=10)

class Customer(models.Model):
    customerId = models.IntegerField(primary_key=True,auto_created=True)
    customerName = models.CharField(max_length=20)
    customerTin = models.CharField(max_length=10)

class Purchase(models.Model):
    purchaseId = models.IntegerField(primary_key=True,auto_created=True)
    date = models.DateTimeField()
    quantity = models.IntegerField()
    totalPrice = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Sale(models.Model):
    saleId = models.IntegerField(primary_key=True,auto_created=True)
    date = models.DateTimeField()
    quantity = models.IntegerField()
    totalPrice = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

#stock is the quantity of the product left
class Stock(models.Model):
    stockId = models.IntegerField(primary_key=True,auto_created=True)
    stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=None,null=False)
