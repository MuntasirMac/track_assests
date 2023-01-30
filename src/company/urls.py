from django.urls import path, include
from company.views import (CreateCompanyView, 
UpdateCompanyView, 
GetAllCompanyView,
GetCompanyDetailsView,
DeleteCompanyView,
)

urlpatterns = [
    path('create-company/', CreateCompanyView.as_view(), name='create-company'),
    path('get-all-company/', GetAllCompanyView.as_view(), name='all-company'),
    path('update-company/<str:company_uid>/', UpdateCompanyView.as_view(), name='update-company'),
    path('company-details/<str:company_uid>/', GetCompanyDetailsView.as_view(), name='company-details'),
    path('delete-company/<str:company_uid>/', DeleteCompanyView.as_view(), name='delete-company'),   
]