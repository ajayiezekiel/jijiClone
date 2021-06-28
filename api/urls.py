from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView
from .views import BuyerAPIView


urlpatterns = [
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('buyers/', BuyerAPIView.as_view()),
]