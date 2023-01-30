from django.db import models
from company.models import Company
import uuid

class Employee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    nid = models.CharField(max_length=32, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)