import uuid
from django.db import models
from employees.models import Employee

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    product_type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    specs = models.TextField()
    buying_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    
class AssignedProduct(models.Model):
    STATE_OKAY = 'O'
    STATE_ABNORMAL = 'A'
    STATE_DEAD = 'D'

    STATE_CHOICES = [
        (STATE_OKAY, 'Okay'),
        (STATE_ABNORMAL, 'Abnormal'),
        (STATE_DEAD, 'Dead'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    assigned_to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_state = models.CharField(max_length=1, choices=STATE_CHOICES, default=STATE_OKAY)
    returned_date = models.DateTimeField(auto_now=True, null=True)
    returned_state = models.CharField(max_length=1, choices=STATE_CHOICES, default=STATE_OKAY)