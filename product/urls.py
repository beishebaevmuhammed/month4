from django.urls import path
from product import views

urlpatterns = [
#     path('hello/', views.hello_view),
#     path('current_date/', views.current_date_view),
#     path('goodbye/', views.goodbye_view),
    path('', views.main_view),
    path('products/', views.product_view),
    path('categories/', views.category_view),
    path('products/<int:product_id>/', views.product_detail_view),
    path('products/create/', views.product_create_view),
    path('categories/create/', views.category_create_view),
]