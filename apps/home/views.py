from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from tenant.models import Tenant
from tenant.utils import get_current_request

def home(request):

    p1 = Product(
        name="New",
        value=1,
    )
    p1.save()
    return HttpResponse('Estou na home')