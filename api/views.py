from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Product, Buyer
from .serializers import BuyerSerializer, ProductSerializer
from .permissions import IsAuthorOrReadOnly


class ProductAPIView(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        if self.request.user.is_authenticated:
                queryset = Product.objects.filter(seller=self.request.user)
                if category:
                    queryset = Product.objects.filter(category=category, seller=self.request.user)
        else:
            queryset = Product.objects.all()
            if category:
                queryset = Product.objects.filter(category=category)
            
        
        return queryset

    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BuyerAPIView(generics.ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

