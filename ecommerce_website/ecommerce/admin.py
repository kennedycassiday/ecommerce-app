from django.contrib import admin
from .models import Category, Product

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
