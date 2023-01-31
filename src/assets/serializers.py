from email.policy import default
from rest_framework import serializers
from employees.serializers import CreateEmployeeSerializer
from assets.models import Product, AssignedProduct

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UpdateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, required=False)
    product_type = serializers.CharField(max_length=32, required=False)
    model = serializers.CharField(max_length=32, required=False)
    specs = serializers.CharField(max_length=2048, required=False)
    
class AssignToEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedProduct
        fields = '__all__'
        
class ReturnAssetSerializer(serializers.Serializer):
    tag = serializers.CharField(max_length=16)
    product = serializers.CharField(max_length=8)
    assigned_to_employee = serializers.CharField(max_length=8)
    returned_state = serializers.CharField(max_length=1, required=False)