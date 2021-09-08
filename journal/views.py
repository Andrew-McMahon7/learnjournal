from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import Resource
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView 

# Create your views here.

def index(request):
    output = "Hello World"
    resources = Resource.objects.all()
    template = loader.get_template('resources.html')
    resource_list = ", ".join([r.name for r in resources])
    context = {
        'resources': resources,
    }
    return HttpResponse(template.render(context, request))


class ResourceView(generic.ListView):
    template_name = 'resources.html'
    context_object_name = 'resources'

    def get_queryset(self):
        """Return the last five published questions."""
        return Resource.objects.order_by('name')  #order_by('-pub_date')[:5]


class ResourceCreateView(CreateView):
    model = Resource
    fields = ['name', 'url']

class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['name', 'url']

# class ResourceDeleteView(DeleteView):
#     model = Resource
#     success_url = reverse_lazy('Resource-list')