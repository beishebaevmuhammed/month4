from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product, Category


# Create your views here.

# def hello_view(request):
#     return HttpResponse("Hello, it's my project")
#
#
# def current_date_view(request):
#     current = datetime.now()
#     return HttpResponse(current)
#
#
# def goodbye_view(request):
#     return HttpResponse("Goodbye!!!")

def main_view(request):
    return render(request, 'index.html')


def product_view(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products/products.html', context=context)


def category_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'products/categories.html', context=context)


def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse('404')
    context = {
        "product": product,
    }
    return render(request, 'products/products_detail.html', context=context, )
