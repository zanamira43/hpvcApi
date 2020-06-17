from django.shortcuts import render
from rest_framework import viewsets, generics

from moneytransfer import serializers
from core.models import Transfer



class TransferListView(generics.ListAPIView):
  """Money Transfer List View"""
  queryset = Transfer.objects.all()
  serializer_class = serializers.TransferSerializer
  
class CreateNewTransfer(generics.CreateAPIView):
  """Moeny Transfer Create Methods"""
  queryset = Transfer.objects.all()
  serializer_class = serializers.TransferSerializer

class TransferDetailView(generics.RetrieveUpdateDestroyAPIView):
  """Money Transfer Detail view"""
  queryset = Transfer.objects.all()
  serializer_class = serializers.TransferSerializer