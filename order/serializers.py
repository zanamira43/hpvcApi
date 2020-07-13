from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Order

class OrderSerialzier(serializers.ModelSerializer):
  """Order Serializer"""
  
  class Meta:
    model = Order
    fields = ('id', 'name', 'quantity', 'rquantity', 'price', 'description', 'image', 'created', 'updated', 'accepted', 'received')
    read_only_fields = ('id', 'created', 'updated', 'image', 'accepted', 'received')
    
    
class OrderImageSerializer(serializers.ModelSerializer):
  """Serializer for upload images to order"""
  class Meta:
    model = Order
    fields = ('id','image')
  
class OrderAcceptedSerializer(serializers.ModelSerializer):
  """create order serializer for accepted confirmation"""
  class Meta:
    model = Order
    fields = ('id', 'accepted')

class OrderRecievedSerializer(serializers.ModelSerializer):
  """create order serializer for received confirmation"""
  class Meta:
    model = Order
    fields = ('id', 'received')