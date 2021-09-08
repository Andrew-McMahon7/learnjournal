from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('resource_generics', views.ResourceView.as_view(), name='resources'),
    path('resource_create', views.ResourceCreateView.as_view(), name='resources_create'),
    path('resource_update', views.ResourceUpdateView.as_view(), name='resources_update'),
]