from django.db import models



class Brand(models.Model):
    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"
    
    # FIELDS
    name = models.CharField(
        verbose_name="vehicle brand (e.g: Toyota)",
        max_length=32, unique=True, blank=False
    )
    
    # METHODS
    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    class Meta:
        verbose_name = "model"
        verbose_name_plural = "models"

    # FIELDS
    name = models.CharField(
        verbose_name="vehicle model (e.g: Hilux)",
        max_length=64, unique=False, blank=False
    )
    brand = models.ForeignKey(
        to=Brand, on_delete=models.RESTRICT,
        verbose_name="vehicle brand (reference)",
    )

    # METHODS
    def __str__(self) -> str:
        return f'{self.brand.name} {self.name}'


class Category(models.Model):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    # FIELDS
    name = models.CharField(
        verbose_name="vehicle category (e.g: SUV)",
        max_length=64, unique=True, blank=False
    )

    # METHODS
    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    class Meta:
        verbose_name = "vehicle"
        verbose_name_plural = "vehicles"
    
    # FIELDS
    model = models.ForeignKey(
        to=Model, on_delete=models.RESTRICT,
        verbose_name="vehicle model (reference)"
    )
    model_year = models.IntegerField(
        verbose_name="model year",
        blank=False,
    )
    categories = models.ManyToManyField(
        to=Category,
    )
    price = models.FloatField(
        verbose_name="price in ARS",
    )
    thumbnail = models.ImageField(
        verbose_name="vehicle image (thumbnail)",
        upload_to="vehicle/thumbnail/"
    )
    
    # METHODS
    def __str__(self) -> str:
        return f"{self.model} {self.model_year}"


class VehicleSite(models.Model):
    class Meta:
        verbose_name = "vehicle site"
        verbose_name_plural = "vehicle sites"
    
    # FIELDS
    vehicle = models.OneToOneField(
        to=Vehicle, on_delete=models.CASCADE,
        verbose_name="vehicle (reference)"
    )
    hero_title = models.TextField(
        verbose_name="hero section title", blank=False,
    )
    hero_phrase = models.TextField(
        verbose_name="hero section subtitle", blank=False,
    )
    hero_description = models.TextField(
        verbose_name="hero section paragraph", blank=False,
    )
    hero_image = models.ImageField(
        verbose_name="vehicle image (main)",
        upload_to="vehicle/hero/"
    )

    # METHODS
    def __str__(self) -> str:
        return f"{self.vehicle}"


class SellingPoint(models.Model):
    class Meta:
        verbose_name = "selling point"
        verbose_name_plural = "selling points"
    
    # FIELDS
    website = models.ForeignKey(
        to=VehicleSite, on_delete=models.CASCADE,
        verbose_name="vehicle website (reference)"
    )
    title = models.TextField(
        verbose_name="title", blank=False,
    )
    text = models.TextField(
        verbose_name="description", blank=False,
    )
    image = models.ImageField(
        verbose_name="selling point image",
        upload_to="vehicle/sites/selling/"
    )

    # METHODS
    def __str__(self) -> str:
        return f"{self.website}: {self.title}"


class FeatureDescription(models.Model):
    class Meta:
        verbose_name = "feature description"
        verbose_name_plural = "feature descriptions"

    # FIELDS
    website = models.ForeignKey(
        to=VehicleSite, on_delete=models.CASCADE,
        verbose_name="vehicle website (reference)"
    )
    title = models.TextField(
        verbose_name="title", blank=False,
    )
    text = models.TextField(
        verbose_name="description", blank=False,
    )
    image = models.ImageField(
        verbose_name="feature image",
        upload_to="vehicle/sites/feature/"
    )

    # METHODS
    def __str__(self) -> str:
        return f"{self.website}: {self.title}"
