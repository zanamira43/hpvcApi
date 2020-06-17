from django.urls import path, include


from order import views

app_name = 'order'



urlpatterns = [
  path('image-upload/', views.OrderImageUploadViewset.as_view(), name='image-upload'),
  path('list', views.OrderListViewSet.as_view(), name='order-list'),
  path('detail/<str:slug>/', views.OrderDetailViewSet.as_view(), name='order-detail'),
  path('accepted/<str:slug>', views.OrderAcceptedViewSet.as_view(), name='accepted-order'),
  path('received/<str:slug>', views.OrderReceivedViewSet.as_view(), name='received-order'),
]