import threading
from django.utils.deprecation import MiddlewareMixin
from django.db.models import Q
from .models import Tenant

class RequestMiddleware(MiddlewareMixin):
    request_local = threading.local()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.request_local.current_request = request
        response = self.get_response(request)
        return response
    
class TenantMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        sub_domain, domain = self._separate_domain_and_subdomain(host)

        tenant_id = self._get_tenant(sub_domain, domain)
        self._set_tenant(request, str(tenant_id))

        response = self.get_response(request)
        return response
    
    @staticmethod
    def _remove_port(host):
        return host.split(':')[0]
    
    def _separate_domain_and_subdomain(self, host):
        host = self._remove_port(host)

        if not '.' in host:
            return None, host
        
        split_host = host.split('.')

        if len(split_host) > 2:
            return None, host
         
        return split_host[0], split_host[1]
    
    def _get_tenant(self, sub_domain, domain):

        filter_tenant = Q()

        filter_tenant &= Q(domain=domain)

        if sub_domain:
            filter_tenant &= Q(sub_domain=sub_domain)

        tenant = Tenant.objects.get(filter_tenant)
        return tenant.id
    

    @staticmethod
    def _set_tenant(request, tenant_id):
        request.session['tenant'] = tenant_id
