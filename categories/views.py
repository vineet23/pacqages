from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories.serializer import CategoriesSerializer, CategoriesDetailSerializer
from categories.models import Category
from django.http import Http404
from rest_framework import generics

# Create your views here.
""" class to get the all categories"""


class CategoriesViewSet(APIView):
    """ to get all the categories"""

    def get(self, request):
        categories = Category.objects.all().order_by("id")
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    """ to add a new category """

    def post(self, request):
        data = request.data
        serializer = CategoriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


""" class to work on a specific category"""


class CategoriesDetailViewSet(APIView):
    """ to get the category object """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    """ to get the specific category"""

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)

    """ to update the specific category"""

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoriesSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """to delete a category"""

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" class to get the list of products in a specific category"""


class CategoryDetailView(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategoriesDetailSerializer

    def get(self, request, *args, **kwargs):
        key = self.kwargs[self.lookup_field]
        try:
            category = Category.objects.get(pk=key)
        except Category.DoesNotExist:
            raise Http404
        serializer = CategoriesDetailSerializer(category)
        return Response(serializer.data)
