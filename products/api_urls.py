from django.urls import path, include
from products.views import Productviewset, ProductDetailViewSet, ProductListViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # to get all product or add a new one
    path("all/", Productviewset.as_view(), name="ProductAll"),
    # to get a single product or update or delete a single product
    path("detail/<int:pk>/", ProductDetailViewSet.as_view(), name="product_detail"),
]

