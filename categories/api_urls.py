from django.urls import path, include
from categories.views import (
    CategoriesViewSet,
    CategoriesDetailViewSet,
    CategoryDetailView,
)
from products.views import ProductListViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # to get all the categories or add a new one
    path("all/", CategoriesViewSet.as_view(), name="CategoryAll"),
    # to get the detail or update an category or delete an category
    path("detail/<int:pk>/", CategoriesDetailViewSet.as_view(), name="category_detail"),
    # to get the list of products in a category
    path("detail_list/<int:pk>/", CategoryDetailView.as_view(), name="product_list"),
]

