from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users:me', request=request, format=format),
        'List All orders': reverse('orders:order-list', request=request, format=format),
        'create new order': reverse('orders:image-upload', request=request, format=format),
        'products': reverse('products:products', request=request, format=format)
    })


