from django.shortcuts import render
from base import models as base_models

# Create your views here.

def index(request):
    services=base_models.Service.objects.all()
    context={'services':services}


    return render(request, 'base/index.html',context)



def service_details(request,service_id):
    service=base_models.Service.objects.get(id=service_id)
    context={'service':service}
    return render(request, 'base/service_details.html', context)