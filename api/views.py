from rest_framework import viewsets
import api.models as models 
import api.serializers as serializers

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = models.ModelCustomer.objects.all()
    serializer_class = serializers.CustomerSerializers

class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.ModelProduct.objects.all()
    serializer_class = serializers.ProductSerializers
