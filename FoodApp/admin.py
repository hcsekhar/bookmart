from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import food, Category, Sub_category, Banner

class foodAdmin(ModelAdmin):
    list_display = ('id', 'item_name','category','sub_categories', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'item_name', 'price')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('item_name', 'price')
# Register your models here.
admin.site.register(food, foodAdmin)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Banner)


