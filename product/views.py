from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from product.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
from product.models import Product, Category, Review


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


def product_detail_view(request, product_id=None):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {
            "product": product,
            'form': ReviewCreateForm()
        }
        return render(request, 'products/products_detail.html', context)
    elif request.method == 'POST':
        form = ReviewCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Review.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/products/{product_id}/')
        context = {
            'form': form,
        }
        return render(request, 'products/products_detail.html', context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm()
        }
        return render(request, 'products/products_create.html', context=context, )
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')
        else:
            context = {
                "form": ProductCreateForm()
            }
            return render(request, 'products/products_create.html', context=context, )

def category_create_view(request):
    if request.method == 'GET':
        context = {
            "form": CategoryCreateForm(),
        }
        return render(request, 'products/categories_create.html', context=context)

    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')
        context = {
            "form": form
        }
        return render(request, 'products/categories_create.html', context=context)


