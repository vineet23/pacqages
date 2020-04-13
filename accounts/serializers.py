from rest_framework import serializers
from accounts.models import Account, Address
from django.contrib.auth.hashers import make_password

"""Basic Serializer for account"""


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # this method has been overrided to change hash the password
        # manually, as the form would simply dump the normal string
        # and would cause problems with the related user object
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])

        return super().create(validated_data)

    class Meta:
        model = Account
        fields = "__all__"


"""Serializer for address"""


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    """ used for the foreign key"""

    def to_representation(self, instance):
        self.fields["user"] = AccountSerializer(read_only=True)
        return super(AddressSerializer, self).to_representation(instance)


"""Serializer for account details like address , cards etc """


class AccountDetailSerializer(serializers.ModelSerializer):
    # as it is linked with user , in Address table (address column related name user_address)
    #  we can get it using generic view in view.py
    user_address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = (
            "first_name",
            "last_name",
            "emailid",
            "password",
            "number",
            "birth_date",
            "user_address",
        )

