
from django.contrib import admin
from django.urls import  path, include

from Main.view import DatabaseHealthCheckAPI, HealthCheckAPI



v1_api_patterns=[
    path('company/', include('company.urls')),
    path('employees/', include('employees.urls')),
    
]

urlpatterns = [
    path('', HealthCheckAPI.as_view() ),
    path('database-connection/', DatabaseHealthCheckAPI.as_view()),
    path('api/', include([
        path('v1/', include(v1_api_patterns))
    ]))
]
