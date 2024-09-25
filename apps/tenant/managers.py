from django.db import models
from django.db.models.query import QuerySet
from .utils import get_current_request

class TenantManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        request = get_current_request()
        tenant_id = request.session['tenant']
        return self._queryset_class(self.model).filter(tenant__id=tenant_id)