from rest_framework import serializers

from core.models import Transfer


class TransferSerializer(serializers.ModelSerializer):
  """Transfer serializer"""
  class Meta:
    model = Transfer
    fields = '__all__'
    read_only_fields = ('id', 'created', 'updated')