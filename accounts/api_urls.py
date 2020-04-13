from django.urls import path, include
from accounts.models import Account
from accounts.views import (
    AccountViewSet,
    AccountDetailViewSet,
    AccountDetailView,
    AddressViewSet,
    AddressDetailViewSet,
)
from rest_framework.urlpatterns import format_suffix_patterns

""" url to access the accounts"""
urlpatterns = [
    # to add an account or get all accounts
    path("all/", AccountViewSet.as_view(), name="accounts"),
    # to get an account or update or delete one
    path("detail/<int:pk>/", AccountDetailViewSet.as_view(), name="account_detail"),
    # to get an detail list of an account like its address , cards etc
    path(
        "detail_list/<int:pk>/", AccountDetailView.as_view(), name="account_detail_list"
    ),
    # to get all the address or add an address
    path("address/all/", AddressViewSet.as_view(), name="address"),
    # to get , update , delete a specific address
    path("address/<int:pk>/", AddressDetailViewSet.as_view(), name="address_detail"),
]

