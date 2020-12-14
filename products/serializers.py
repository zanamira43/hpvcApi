from rest_framework import serializers
from .models import Product


class PrdouctSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    # fields = '__all__'
    fields = [
      'title',
      'singular_price',
      'plural_price',
      'photo' ,
      'created_at'
    ]


