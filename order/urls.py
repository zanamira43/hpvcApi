from django.urls import path, include


from order import views

app_name = 'order'



urlpatterns = [
  path('image-upload/', views.OrderImageUploadViewset.as_view(), name='image-upload'),
  path('list', views.OrderListViewSet.as_view(), name='order-list'),
  path('detail/<int:pk>/', views.OrderDetailViewSet.as_view(), name='order-detail'),
  path('accepted/<int:pk>', views.OrderAcceptedViewSet.as_view(), name='accepted-order'),
  path('received/<int:pk>', views.OrderReceivedViewSet.as_view(), name='received-order'),
]