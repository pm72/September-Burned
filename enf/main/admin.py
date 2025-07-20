from django.contrib import admin
from . models import Category, Product, ProductImage, Size, productSize


class ProductImageInline(admin.TabularInline):
  model = ProductImage
  extra = 1


class ProductSizeInline(admin.TabularInline):
  model = productSize
  extra = 1


class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'color', 'price')
  list_filter = ('category', 'color')
  search_fields = ('name', 'color', 'description')
  prepopulated_fields = {'slug': ('name',)}
  inlines = (ProductImageInline, ProductSizeInline)