from django.contrib import admin
from .models import Category, Product, Order

# Register your models here.

@admin.register(Category)
class TodoList(admin.ModelAdmin):
    list_display = (
        "name",
    )

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "price",
        "description",
        "image",
    )

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = (
        "user",
        "total_price",
        "ordered_date",
        "is_ordered",
    )
