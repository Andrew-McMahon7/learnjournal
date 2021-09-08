from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import Resource
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView 
from journal.forms import ResourceForm

# Create your views here.

def index(request):
    resources = Resource.objects.all()


    resource_form = ResourceForm()
    if request.POST:
        resource_form = ResourceForm(request.POST)
        if resource_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.save()

    else :
        resource_form = ResourceForm()


    template = loader.get_template('resources.html')
    context = {
        'resources': resources,
        'resource_form': resource_form,
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