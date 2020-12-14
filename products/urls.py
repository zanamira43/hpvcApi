from django.urls import path, include

from .views import ProductList

app_name = 'products'

urlpatterns = [
  path('products', ProductList.as_view(), name="products")
]
