# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.StockkeeperIndex.as_view(), name='stockkeeper-index'),
        path('categories/<int:parent_id>', views.ComponentTypeListView.as_view(), name='stockkeeper-categories'),
]
