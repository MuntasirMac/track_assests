from django.urls import path, include
from employees.views import (CreateEmployeeView, 
UpdateEmployeeView, 
GetAllEmployeeView,
GetEmployeeDetailsView,
DeleteEmployeeView,
)

urlpatterns = [
    path('create-employee/', CreateEmployeeView.as_view(), name='create-employee'),
    path('get-all-employee/', GetAllEmployeeView.as_view(), name='all-employee'),
    path('update-employee/<str:employee_uid>/', UpdateEmployeeView.as_view(), name='update-employee'),
    path('employee-details/<str:employee_uid>/', GetEmployeeDetailsView.as_view(), name='employee-details'),
    path('delete-employee/<str:employee_uid>/', DeleteEmployeeView.as_view(), name='delete-employee'),  
]