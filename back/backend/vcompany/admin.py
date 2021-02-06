from django.contrib import admin
from django.forms import ModelForm
from .models import SliderModel, Product, News, Category, SinglePage, IndexModel

admin.site.register(SliderModel)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(SinglePage)
admin.site.register(IndexModel)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category']
