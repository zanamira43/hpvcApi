from django.urls import path, include

from moneytransfer import views

app_name = 'moneytransfer'

urlpatterns = [
  path('transfers/', views.TransferListView.as_view(), name='transfers'),
  path('create_transfer/', views.CreateNewTransfer.as_view(), name="create_transfer"),
  path('transfers/<int:pk>/', views.TransferDetailView.as_view(), name="transfers_detail")
]