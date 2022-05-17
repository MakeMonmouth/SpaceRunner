from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models as account_models

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        if user.is_authenticated:
            print("User is authenticated")
        else:
            context['memberships'] = account_models.MembershipType.objects.select_related()
        return context
            
