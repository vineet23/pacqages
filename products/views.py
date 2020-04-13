from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import Productserializer
from products.models import Product
from django.http import Http404

# Create your views here.
""" to get all the products"""


class Productviewset(APIView):
    """ to get all the products"""

    def get(self, request):
        product = Product.objects.all().order_by("id")
        serializer = Productserializer(product, many=True)
        return Response(serializer.data)

    """ to insert a product """

    def post(self, request):
        data = request.data
        serializer = Productserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ProductDetailViewSet(APIView):
    """ to get the product object """

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    """ to get the specific product"""

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = Productserializer(category)
        return Response(serializer.data)

    """ to update the specific product"""

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = Productserializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """to delete a product"""

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" to get all the products of a specific category"""
"""NOTE not used any more"""


class ProductListViewSet(APIView):
    """ to get all the product list"""

    def get(self, request, pk, format=None):
        product = Product.objects.filter(category_id=pk).order_by("id")
        serializer = Productserializer(product, many=True)
        return Response(serializer.data)

