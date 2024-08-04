from django.contrib import admin

# Register your models here.

from .models import Product, Contact, Email, Order, Order_Update

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(Order)
admin.site.register(Order_Update)
