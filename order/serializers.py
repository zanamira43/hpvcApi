from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Order

class OrderSerialzier(serializers.ModelSerializer):
  """Order Serializer"""
  
  class Meta:
    model = Order
    fields = ('id','slug', 'name', 'quantity', 'rquantity', 'price', 'description', 'image', 'created', 'updated', 'accepted', 'received')
    read_only_fields = ('id', 'slug', 'created', 'updated', 'image', 'accepted', 'received')
    
    
class OrderImageSerializer(serializers.ModelSerializer):
  """Serializer for upload images to order"""
  class Meta:
    model = Order
    fields = ('id','slug','image')
    read_only_fields = ('id', 'slug')
  
class OrderAcceptedSerializer(serializers.ModelSerializer):
  """create order serializer for accepted confirmation"""
  class Meta:
    model = Order
    fields = ('id', 'slug', 'accepted')
    read_only_fields = ('id', 'slug')

class OrderRecievedSerializer(serializers.ModelSerializer):
  """create order serializer for received confirmation"""
  class Meta:
    model = Order
    fields = ('id', 'slug', 'received')
    read_only_fields = ('id', 'slug')