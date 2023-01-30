from django.urls import path, include
from assets.views import (CreateProductView, 
UpdateProductView, 
GetAllProductView,
GetProductDetailsView,
DeleteProductView,
)

urlpatterns = [
    path('create-product/', CreateProductView.as_view(), name='create-product'),
    path('get-all-product/', GetAllProductView.as_view(), name='all-product'),
    path('update-product/<str:product_uid>/', UpdateProductView.as_view(), name='update-product'),
    path('product-details/<str:product_uid>/', GetProductDetailsView.as_view(), name='product-details'),
    path('delete-product/<str:product_uid>/', DeleteProductView.as_view(), name='delete-product'),   
]