from rest_framework import serializers
from products.models import Product
from categories.models import Category

""" define here to use bellow"""


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


""" to give the api for products"""


class Productserializer(serializers.ModelSerializer):
    """ for getting the category associated with the product"""

    class Meta:
        model = Product
        fields = ("id", "name", "price", "discount", "category", "diet", "unit")

    """ used for the foreign key"""

    def to_representation(self, instance):
        self.fields["category"] = CategoriesSerializer(read_only=True)
        return super(Productserializer, self).to_representation(instance)
