from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404


from .models import StorageArea
from .models import ComponentType


class StockkeeperIndex(ListView):

    model = ComponentType
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return ComponentType.objects.filter(parent_id=None).order_by("name")

class ComponentTypeListView(ListView):

    model = ComponentType
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        self.parent = get_object_or_404(ComponentType, id=self.kwargs['parent_id'])
        return ComponentType.objects.filter(parent=self.parent).order_by("name")
