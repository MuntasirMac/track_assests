from rest_framework import serializers
from company.serializers import CreateCompanySerializer
from employees.models import Employee

class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class UpdateEmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128, required=False)
    designation = serializers.CharField(max_length=128, required=False)
    phone = serializers.CharField(max_length=32, required=False)
    nid = serializers.CharField(max_length=32, required=False)
    company = serializers.CharField(max_length=128, required=False)
    
class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    company = CreateCompanySerializer()