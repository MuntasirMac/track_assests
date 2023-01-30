from company.serializers import (CreateCompanySerializer, 
                                 UpdateCompanySerializer
                            )
from company.models import Company
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateCompanyView(APIView):
    def post(self, request, format=None):
        create_company_serializer = CreateCompanySerializer(data=request.data)
        
        if create_company_serializer.is_valid():
            create_company_serializer.save()
            
            print(create_company_serializer.data)
            
            return Response({'data': create_company_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_company_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class GetAllCompanyView(APIView):
    def get(self, request, format=None):
        all_companies = Company.objects.all().values()
        return Response({'data':all_companies}, status=status.HTTP_200_OK)
    
class GetCompanyDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        company_uid = kwargs.get('company_uid')
        if company_uid:
            company_details = Company.objects.filter(uuid=company_uid).values()
            print(company_details)
            return Response({'data':company_details}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Company Invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateCompanyView(APIView):
    def put(self, request, *args, **kwargs):
        company_uid = kwargs.get('company_uid')
        company_update_serializer= UpdateCompanySerializer(data= request.data)

        if company_update_serializer.is_valid():

            company_update_data = company_update_serializer.validated_data

            company = Company.objects.filter(uuid = company_uid).first()
            print(company)

            update_company = Company.objects.filter(uuid = company_uid).update(
                                        name=company_update_data.get('name', company.name),
                                        cell = company_update_data.get('cell', company.cell),
                                        address = company_update_data.get('address', company.address),
                                        )


            print(update_company)

            if update_company: 
                update_company = Company.objects.filter(uuid = company_uid).first()         
                return Response({'data' : model_to_dict(update_company)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': company_update_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteCompanyView(APIView):
    def delete(self, request, *args, **kwargs):
        company_uid = kwargs.get('company_uid')
        company = Company.objects.filter(uuid=company_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)