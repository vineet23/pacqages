from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    discount = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_detail"
    )
    diet = models.BooleanField(blank=False, null=False)
    unit = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name

