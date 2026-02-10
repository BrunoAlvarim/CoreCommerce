from rest_framework import serializers
import api.models as models

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCustomer
        exclude = ['created_at','hash_id']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ModelProduct
        exclude = ['created_at','hash_id']
