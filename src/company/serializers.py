from rest_framework import serializers
from company.models import Company

class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class UpdateCompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    cell = serializers.CharField(max_length=32, required=False)
    address = serializers.CharField(max_length=512, required=False)