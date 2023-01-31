from itertools import product
from urllib import request
from assets.serializers import (CreateProductSerializer, 
                                 UpdateProductSerializer,
                                 AssignToEmployeeSerializer,
                                 ReturnAssetSerializer
                            )
from assets.models import Product, AssignedProduct
from datetime import datetime, date
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateProductView(APIView):
    def post(self, request, format=None):
        create_product_serializer = CreateProductSerializer(data=request.data)
        
        if create_product_serializer.is_valid():
            create_product_serializer.save()
            
            print(create_product_serializer.data)
            
            return Response({'data': create_product_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class GetAllProductView(APIView):
    def get(self, request, format=None):
        all_companies = Product.objects.all().values()
        return Response({'data':all_companies}, status=status.HTTP_200_OK)
    
class GetProductDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        product_uid = kwargs.get('product_uid')
        if product_uid:
            product_details = Product.objects.filter(uuid=product_uid).values()
            print(product_details)
            return Response({'data':product_details}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Product Invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateProductView(APIView):
    def put(self, request, *args, **kwargs):
        product_uid = kwargs.get('product_uid')
        product_update_serializer= UpdateProductSerializer(data= request.data)

        if product_update_serializer.is_valid():

            product_update_data = product_update_serializer.validated_data

            product = Product.objects.filter(uuid = product_uid).first()
            print(product)

            update_product = Product.objects.filter(uuid = product_uid).update(
                                        name=product_update_data.get('name', product.name),
                                        product_type = product_update_data.get('product_type', product.product_type),
                                        model = product_update_data.get('model', product.model),
                                        specs = product_update_data.get('specs', product.specs)
                                        )


            print(update_product)

            if update_product: 
                updated_product = Product.objects.filter(uuid = product_uid).first()         
                return Response({'data' : model_to_dict(updated_product)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': product_update_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteProductView(APIView):
    def delete(self, request, *args, **kwargs):
        product_uid = kwargs.get('product_uid')
        product = Product.objects.filter(uuid=product_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AssignToEmployeeView(APIView):
    def post(self, request, format=None):
        assign_product_serializer = AssignToEmployeeSerializer(data=request.data)
        
        if assign_product_serializer.is_valid():
            product_to_assign = assign_product_serializer.validated_data
            print(product_to_assign)
            check_assigned_product = AssignedProduct.objects.filter(tag=product_to_assign.get('tag'), product=product_to_assign.get('product')).order_by('-assigned_date').first()
            if check_assigned_product:
                last_returned = check_assigned_product.get('returned_date')
                if date.today() > last_returned:
                    assign_product_serializer.save()
                    return Response({'data': assign_product_serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': "The product is in use now"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                assign_product_serializer.save()
                return Response({'data': assign_product_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': assign_product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class ReturnAssetView(APIView):
    def post(self, request, format=None):
        return_asset_serializer = ReturnAssetSerializer(data=request.data)
        
        if return_asset_serializer.is_valid():
            return_asset_data = return_asset_serializer.validated_data
            print(return_asset_data)
            asset_to_return = AssignedProduct.objects.filter(tag=return_asset_data.get('tag'),
                                                        product=return_asset_data.get('product'),
                                                        assigned_to_employee=return_asset_data.get('assigned_to_employee'),
                                                    ).order_by('-assigned_date').first()
            print(asset_to_return)
            returned_asset = AssignedProduct.objects.create(tag=asset_to_return.tag,
                                                        product=asset_to_return.product,
                                                        assigned_to_employee=asset_to_return.assigned_to_employee,
                                                        returned_state = return_asset_data.get('returned_state'),
                                                        assigned_date = asset_to_return.assigned_date,
                                                        returned_date = datetime.now()
                                                    )
            
            return Response({'data':model_to_dict(returned_asset)}, status=status.HTTP_200_OK)
        else:
            return Response({'data': return_asset_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)