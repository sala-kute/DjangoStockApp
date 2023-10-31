from django.shortcuts import render, redirect 
from .models import Product, Sale , Stock , Customer , Purchase , Supplier
from datetime import date
from django.contrib import messages

def error(request):
    error_message = request.session.pop('error_message', None)
    return render(request, 'StockApp/error.html', {'error_message': error_message})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'StockApp/product_list.html', {'products': products})

def dashboard(request):
    return render(request, 'StockApp/dashboard.html', )

def stock_list(request):
    stocks = Stock.objects.raw('''
        SELECT StockApp_stock.*, StockApp_product.*
        FROM StockApp_stock
        INNER JOIN StockApp_product ON StockApp_stock.product_id = StockApp_product.productId
    ''')
    context = {'stocks': stocks}
    return render(request, 'StockApp/stock_list.html', context)

def sales_list(request):
    sales = Sale.objects.raw('''
        SELECT StockApp_sale.*, StockApp_product.*, StockApp_customer.*
        FROM StockApp_sale
        INNER JOIN StockApp_product ON StockApp_sale.product_id = StockApp_product.productId
        INNER JOIN StockApp_customer ON StockApp_sale.customer_id = StockApp_customer.customerId
    ''')
    context = {'sales': sales}
    return render(request, 'StockApp/sales_list.html', context)

def purchase_list(request):
    purchases = Purchase.objects.raw('''
        SELECT StockApp_purchase.*, StockApp_product.*, StockApp_supplier.*
        FROM StockApp_purchase
        INNER JOIN StockApp_product ON StockApp_purchase.product_id = StockApp_product.productId
        INNER JOIN StockApp_supplier ON StockApp_purchase.supplier_id = StockApp_supplier.supplierId
    ''')
    context = {'purchases': purchases}
    return render(request, 'StockApp/purchase_list.html', context)

def add_sale(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity', 0))
        customerName = request.POST.get('customerName')
        customerTin= request.POST.get('customerTin')

        product = Product.objects.get(productId=product_id)
        price = product.price
        total_price = price * quantity
        
        stock = Stock.objects.get(product=product)
        if quantity > stock.stock:
            error_message = 'Insufficient stock for the selected product.'
            request.session['error_message'] = error_message
            error_message = 'Insufficient stock for the selected product.'
            return redirect('error')
        
        customer = Customer.objects.filter(
            customerName=customerName,
            customerTin=customerTin
        ).order_by('-customerId').first()

        if not customer:
            customer = Customer.objects.create(
                customerName=customerName,
                customerTin=customerTin
            )

        customer.save()

        sale = Sale.objects.create(
            quantity=quantity,
            date=date.today(),
            totalPrice=total_price,
            product=product,
            customer=customer
        )


        # Update stock
        stock = Stock.objects.get(product=product)
        stock.stock -= quantity
        stock.save()
        
        return redirect('sales_list')  # Redirect to the sales list page
    
    context = {'products': products,}
    return render(request, 'StockApp/add_sale.html', context)

def add_purchase(request):
    products = Product.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        supplier_id = request.POST.get('supplier')
        quantity = int(request.POST.get('quantity', 0))

        product = Product.objects.get(productId=product_id)
        price = product.price
        total_price = price * quantity
        
        supplier = Supplier.objects.get(supplierId=supplier_id)


        purchase = Purchase.objects.create(
            quantity=quantity,
            date=date.today(),
            totalPrice=total_price,
            product=product,
            supplier=supplier
        )


        # Update stock
        stock = Stock.objects.get(product=product)
        stock.stock += quantity
        stock.save()
        
        return redirect('purchase_list')  # Redirect to the sales list page
    
    context = {'products': products, 'suppliers': suppliers}
    return render(request, 'StockApp/add_purchase.html', context)
  
# Add other views for purchase, sale, supplier, customer, and stock as needed