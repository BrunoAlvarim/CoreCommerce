from rest_framework import viewsets
import api.models as models 
import api.serializers as serializers

class UserViewSet(viewsets.ModelViewSet):

    queryset = models.ModelCustomer.objects.all()
    serializer_class = serializers.CustomerSerializers
