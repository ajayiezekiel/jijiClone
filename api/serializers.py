from rest_framework import serializers
from .models import Product, Buyer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'location', 'imageUrl', 'isSold', 'seller', 'category', 'createdAt' )


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ('name', 'phoneNumber', 'emailAddress', 'product')
