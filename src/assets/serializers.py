from rest_framework import serializers
from employees.serializers import CreateEmployeeSerializer
from assets.models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UpdateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, required=False)
    product_type = serializers.CharField(max_length=32, required=False)
    model = serializers.CharField(max_length=32, required=False)
    specs = serializers.CharField(max_length=2048, required=False)
    
