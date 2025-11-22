from django.db import models
from django.contrib import admin
class Product(models.Model):
    ProductID=models.CharField(primary_key=True,max_length=8)
    ProductName=models.TextField()
    Price=models.FloatField()
    ProductType=models.TextField()
    SupplierName=models.TextField()
    Ratings=models.FloatField()

class ProductAdmin(admin.ModelAdmin):
    list_display=["ProductID","ProductName","Price","ProductType","SupplierName","Ratings"]

