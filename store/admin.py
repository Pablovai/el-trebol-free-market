from django.contrib import admin
from .models import Product 

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    search_fields = ('product_name',)
    list_per_page = 10 
    
admin.site.register(Product, ProductAdmin)  
    