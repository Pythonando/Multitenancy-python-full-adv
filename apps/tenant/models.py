from django.db import models
import uuid
from .validators import validate_cnpj
from .managers import TenantManager
from .utils import get_current_request

# Create your models here.
class BaseTenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    cnpj = models.CharField(max_length=100, validators=[validate_cnpj,])
    company_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Tenant(BaseTenant):
    domain = models.CharField(max_length=255, unique=True, null=True, blank=True)
    sub_domain = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.sub_domain}.{self.domain}'
    
class TenantModel(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    objects = TenantManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        request = get_current_request()
        if not self.tenant:
            self.tenant = Tenant.objects.get(id=request.session['tenant'])

        super(TenantModel, self).save(*args, **kwargs)