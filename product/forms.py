from django import forms

from product.models import Product, Review, Category


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'image', 'rate', 'category') # Поля которые мы хоти видеть взятые из моделек


class CategoryCreateForm(forms.ModelForm):
    class Meta: # Мы можем указать класс который хотим унасследовать
        model = Category
        fields = ('title',)


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)