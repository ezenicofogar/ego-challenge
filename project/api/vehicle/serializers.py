from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Brand, Model, Category, Vehicle, VehicleSite, SellingPoint, FeatureDescription

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 2

class SellingPointSerializer(ModelSerializer):
    class Meta:
        model = SellingPoint
        fields = ['title', 'text', 'image',]

class FeatureDescriptionSerializer(ModelSerializer):
    class Meta:
        model = FeatureDescription
        fields = ['title', 'text', 'image',]

class VehicleSiteSerializer(ModelSerializer):
    sellingpoint_set = SellingPointSerializer(many=True, read_only=True)
    featuredescription_set = FeatureDescriptionSerializer(many=True, read_only=True)
    class Meta:
        model = VehicleSite
        fields = ['hero_title', 'hero_phrase', 'hero_description', 'hero_image', 'sellingpoint_set', 'featuredescription_set',]
        depth = 2

class VehicleDetailSerializer(ModelSerializer):
    vehiclesite = VehicleSiteSerializer(many=False, read_only=True)
    class Meta:
        model = Vehicle
        fields = ['model', 'model_year', 'categories', 'price', 'thumbnail', 'vehiclesite',]
        depth = 2
