from django.shortcuts import render, get_object_or_404
from .models import Product


def product(request, pk):
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', {
        'products': products,
        'product': product
    })