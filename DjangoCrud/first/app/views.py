from django.shortcuts import render, redirect
from .models import Product
from django.db import IntegrityError

def index(request):
    if request.method == 'POST':
        if 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            Product.objects.filter(id=delete_id).delete()
            # Renumber IDs after deletion
            renumber_ids()
        else:
            try:
                product_id = request.POST.get('product_id')
                if product_id:
                    product = Product.objects.get(id=product_id)
                    product.name = request.POST.get('name')
                    product.details = request.POST.get('details')
                    product.quality = request.POST.get('quality')
                    product.product_type = request.POST.get('product_type')
                    product.quantity = request.POST.get('quantity')
                    product.price = request.POST.get('price')
                    product.manufacture_date = request.POST.get('manufacture_date')
                    product.available = 'available' in request.POST
                    product.rating = request.POST.get('rating')
                    product.save()
                else:
                    # Create a new product with the next available ID
                    new_id = get_next_available_id()
                    Product.objects.create(
                        id=new_id,
                        name=request.POST.get('name'),
                        details=request.POST.get('details'),
                        quality=request.POST.get('quality'),
                        product_type=request.POST.get('product_type'),
                        quantity=request.POST.get('quantity'),
                        price=request.POST.get('price'),
                        manufacture_date=request.POST.get('manufacture_date'),
                        available='available' in request.POST,
                        rating=request.POST.get('rating')
                    )
                # Renumber IDs after creation
                renumber_ids()
            except IntegrityError:
                return render(request, 'index.html', {'error': 'An error occurred'})

        return redirect('index')

    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query).order_by('id')
    else:
        products = Product.objects.all().order_by('id')

    return render(request, 'index.html', {'products': products})

def get_next_available_id():
    # Get the next available ID, considering existing IDs and gaps
    existing_ids = Product.objects.values_list('id', flat=True).order_by('id')
    if existing_ids:
        return existing_ids.last() + 1
    return 1

def renumber_ids():
    products = Product.objects.all().order_by('id')
    for index, product in enumerate(products, start=1):
        product.id = index
        product.save()
