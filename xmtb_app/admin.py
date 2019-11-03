from django.contrib import admin
from .models import *

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Products._meta.get_fields()]

admin.site.register(Cities)
admin.site.register(Brands)
admin.site.register(Categories)
