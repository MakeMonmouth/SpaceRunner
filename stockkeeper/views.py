from django.http import HttpResponse
from django.template import loader

from .models import StorageArea


def index(request):
    storage_areas = StorageArea.objects.order_by('-storage_area_name')
    template = loader.get_template('stockkeeper/index.html')
    context = {
        'stock_areas': storage_areas,
    }
    return HttpResponse(template.render(context, request))
