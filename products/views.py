from django.shortcuts import render
from rest_framework import response
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from .serializers import PrdouctSerializer
from .models import Product



class ProductList(generics.GenericAPIView, mixins.ListModelMixin):
  """
    List All Product and list New One
  """

  queryset = Product.objects.all()
  serializer_class = PrdouctSerializer

  def get(self, request, pk=None):

    if pk:

      return response({
        "data": self.retrieve(request, pk).data
      }, status=status.HTTP_200_OK)

    return self.list(request)

