from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product


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

