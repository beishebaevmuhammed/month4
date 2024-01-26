from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.title
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return self.text






