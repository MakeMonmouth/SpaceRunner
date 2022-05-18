from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models as account_models
from stockkeeper import models as sk_models

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        if user.is_authenticated:
            context['user'] = user
            component_types = []
            for ct in sk_models.ComponentType.objects.all().order_by("name"):
                if ct.component_set.count() > 0:
                    component_types.append(
                            {
                                "id": ct.id,
                                "name": ct.name,
                                "qty": ct.component_set.count()
                                }
                            )
            context['component_types'] = component_types
        else:
            context['memberships'] = account_models.MembershipType.objects.select_related()
        return context
            
