from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('allResources', views.ResourceView.as_view(), name='resources'),
    path('allTagResources', views.TagResourceView.as_view(), name='resources_tags'),
    path('allContactResources', views.ContactResourceView.as_view(), name='resources_contacts'),
    path('createResource', views.ResourceCreateView.as_view(), name='resource_create'),
    path('createTag', views.TagCreateView.as_view(), name='tag_resource_create'),
    path('createContact', views.ContactCreateView.as_view(), name='contact_resource_create'),
    path('updateResource/<int:pk>', views.ResourceUpdateView.as_view(), name='resource_update'),
    path('updateContact/<int:pk>', views.ContactUpdateView.as_view(), name='contact_update'),
    path('updateTag/<int:pk>', views.TagUpdateView.as_view(), name='tag_update'),
    path('deleteResource/<int:pk>', views.ResourceDeleteView.as_view(), name='resource_delete'),
    path('deleteContact/<int:pk>', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('deleteTag/<int:pk>', views.TagDeleteView.as_view(), name='tag_delete'),
    re_path(r'^sendmail/(?P<contact_id>\d+)/(?P<resource_id>\d+)$', views.sendmail, name='sendmail'),
]