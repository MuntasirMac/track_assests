from django.forms import model_to_dict
from employees.models import Employee
from employees.serializers import CreateEmployeeSerializer, UpdateEmployeeSerializer, EmployeeDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateEmployeeView(APIView):
    def post(self, request, format=None):
        create_employee_serializer = CreateEmployeeSerializer(data=request.data, many=True)
        
        if create_employee_serializer.is_valid():
            create_employee_serializer.save()
            
            print(create_employee_serializer.data)
            
            return Response({'data': create_employee_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class GetAllEmployeeView(APIView):
    def get(self, request, format=None):
        all_employee = Employee.objects.all().values()
        return Response({'data':all_employee}, status=status.HTTP_200_OK)
    
class GetEmployeeDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        employee_uid = kwargs.get('employee_uid')
        if employee_uid:
            employee = Employee.objects.filter(uuid=employee_uid).first()
            employee_details = EmployeeDetailSerializer(employee)
            print(employee_details.data)
            return Response({'data':employee_details.data}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Employee Invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateEmployeeView(APIView):
    def put(self, request, *args, **kwargs):
        employee_uid = kwargs.get('employee_uid')
        employee_update_serializer= UpdateEmployeeSerializer(data= request.data)

        if employee_update_serializer.is_valid():

            employee_update_data = employee_update_serializer.validated_data

            employee = Employee.objects.filter(uuid = employee_uid).first()
            print(employee)

            update_employee = Employee.objects.filter(uuid = employee_uid).update(
                                        name=employee_update_data.get('name', employee.name),
                                        designation = employee_update_data.get('designation', employee.designation),
                                        phone = employee_update_data.get('phone', employee.phone),
                                        nid = employee_update_data.get('nid', employee.nid),
                                        company = employee_update_data.get('company', employee.company),
                                        )


            print(update_employee)

            if update_employee: 
                update_employee = Employee.objects.filter(uuid = employee_uid).first()
                updated_employee = EmployeeDetailSerializer(update_employee)       
                return Response({'data' : updated_employee.data},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': employee_update_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteEmployeeView(APIView):
    def delete(self, request, *args, **kwargs):
        employee_uid = kwargs.get('employee_uid')
        employee = Employee.objects.filter(uuid=employee_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)