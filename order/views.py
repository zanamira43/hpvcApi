from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from core.models import Order
from order import serializers

class OrderImageUploadViewset(generics.CreateAPIView):
  """Upload Image view for order model"""
  serializer_class = serializers.OrderImageSerializer
  queryset = Order.objects.all()

class OrderListViewSet(generics.ListAPIView):
  serializer_class = serializers.OrderSerialzier
  queryset = Order.objects.all()
  
  def list(self, request, *args, **kwargs):
    queryset = Order.objects.order_by('-id')
    serilizer = self.get_serializer(queryset, many=True)
    items = {'items': serilizer.data}
    return Response(items)

class OrderDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = serializers.OrderSerialzier
  queryset = Order.objects.all()
  

class OrderAcceptedViewSet(generics.RetrieveUpdateAPIView):
  """update orders accepted view"""
  serializer_class = serializers.OrderAcceptedSerializer
  queryset = Order.objects.all()
  
  
class OrderReceivedViewSet(generics.RetrieveUpdateAPIView):
  """ update orders received view"""
  serializer_class = serializers.OrderRecievedSerializer
  queryset = Order.objects.all()