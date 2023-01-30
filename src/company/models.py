import uuid
from django.db import models

# Create your models here.
class Company(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    cell = models.CharField(max_length=32)
    address = models.CharField(max_length=512)