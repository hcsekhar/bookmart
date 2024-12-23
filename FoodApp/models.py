from datetime import datetime

from django.db import models
from reportlab.graphics.samples.excelcolors import color01, color02
from unicodedata import category

from Food.settings import DEFAULT_AUTO_FIELD


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(null=True, blank=False)
    category_colour = models.TextField(null=True, blank=False)
    def __str__(self):
        return self.category_name

class Sub_category(models.Model):
    sub_category_image = models.ImageField(null=False, blank=False)
    sub_category_name = models.CharField(max_length=100)
    main_category= models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.sub_category_name


class food(models.Model):
    image = models.ImageField(null=False,blank=False)
    item_name = models.CharField(null=False,blank=False,max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    sub_categories = models.ForeignKey(Sub_category, on_delete=models.CASCADE, default=True, null=False)
    price = models.DecimalField(null=False,blank=False,max_digits=6,decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now(),blank=True)

    def __str__(self):
        return self.item_name

class Banner(models.Model):
    banner_img = models.ImageField(null=False, blank=False, upload_to='banners/')
    short_discp = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.title