from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('allResources', views.ResourceView.as_view(), name='resources'),
    path('createResource', views.ResourceCreateView.as_view(), name='resource_create'),
    path('resource_update', views.ResourceUpdateView.as_view(), name='resource_update'),
]