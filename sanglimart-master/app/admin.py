from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','selling_price',
    'discounted_price', 'description', 'brand',
     'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedmodelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',  'product', 'quantity', 'ordered_date', 'status']

# Create Python virtual Enviornment (python -m venv venv , venv\Scripts\activate, pip install django)
# C- django-admin startproject ecomproj
# Add "app" flder into ecomproj
# add app to setting.py in ecomproj
# create Model.py (State choices and class [make Each class for each seprate task])
# Create Superadmin (python manage.py createsuperadmin)
# Make Migration (C- python manage.py makemigrations , python manage.py migrate)
# Create admin.py [Register all the stuff you require in the admin panel in database)

