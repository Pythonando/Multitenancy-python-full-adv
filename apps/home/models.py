from django.db import models
from tenant.models import TenantModel

# Create your models here.
class Product(TenantModel):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return f'{self.name}'