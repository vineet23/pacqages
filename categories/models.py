from django.db import models

# Create your models here.

""" table for categories"""
""" TODO add field for images"""


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    diet = models.BooleanField(blank=False, null=False)
    image = models.ImageField(
        upload_to="category", max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.name

