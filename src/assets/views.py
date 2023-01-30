from assets.serializers import (CreateProductSerializer, 
                                 UpdateProductSerializer
                            )
from assets.models import Product
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
            print(Product)

            update_product = Product.objects.filter(uuid = product_uid).update(
                                        name=product_update_data.get('name', product.name),
                                        product_type = product_update_data.get('product_type', product.product_type),
                                        model = product_update_data.get('model', product.model),
                                        specs = product_update_data.get('specs', product.specs)
                                        )


            print(update_product)

            if update_product: 
                update_product = Product.objects.filter(uuid = product_uid).first()         
                return Response({'data' : model_to_dict(update_product)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': product_update_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteProductView(APIView):
    def delete(self, request, *args, **kwargs):
        product_uid = kwargs.get('product_uid')
        product = Product.objects.filter(uuid=product_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)