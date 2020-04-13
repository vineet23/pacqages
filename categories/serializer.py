from rest_framework import serializers
from categories.models import Category
from products.serializers import Productserializer

""" serializer for categories table"""


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


""" serializer for the nested json with products"""


class CategoriesDetailSerializer(serializers.ModelSerializer):
    # as it is linked with product , in Product table (category column related name category_detail)
    #  we can get it using generic view in view.py
    category_detail = Productserializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "diet", "category_detail")

