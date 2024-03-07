from django.contrib import admin
from .models import Brand, Model, Category, Vehicle, VehicleSite, SellingPoint, FeatureDescription

# Register your models here.
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Category)
admin.site.register(Vehicle)
admin.site.register(VehicleSite)
admin.site.register(SellingPoint)
admin.site.register(FeatureDescription)
