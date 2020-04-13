from django.shortcuts import render
from accounts.models import Account, Address
from accounts.serializers import (
    AccountSerializer,
    AddressSerializer,
    AccountDetailSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics

# Create your views here.
""" to get all accounts or create a new account"""


class AccountViewSet(APIView):
    def get(self, request):
        account = Account.objects.all().order_by("id")
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


""" for a single account"""


class AccountDetailViewSet(APIView):
    """ to get the account object """

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    """ to get the specific account"""

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    """ to update the specific account"""

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """to delete a account"""

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" class to get the list of attributes like address,cards of a specific account"""


class AccountDetailView(generics.ListCreateAPIView):
    # queryset = Account.objects.all()
    # serializer_class = AccountDetailSerializer

    def get(self, request, *args, **kwargs):
        key = self.kwargs[self.lookup_field]
        try:
            account = Account.objects.get(pk=key)
        except Account.DoesNotExist:
            raise Http404
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)


""" for the address"""


class AddressViewSet(APIView):
    """ to get all the address"""

    def get(self, request):
        address = Address.objects.all().order_by("id")
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    """ to insert a address """

    # TODO before posting check that title is unique for the same user
    def post(self, request):
        data = request.data
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


""" for a single address get , update , delete """


class AddressDetailViewSet(APIView):
    """ to get the address object """

    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    """ to get the specific address"""

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    """ to update the specific address"""

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """to delete a address"""

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

