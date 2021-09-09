from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import JournalResource, Resource
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView 
from journal.forms import JournalResourceForm

# Create your views here.

def index(request):
    journalResources = JournalResource.objects.all()
    journalResourceForm = JournalResourceForm()

    if request.POST:
        journalResourceForm = JournalResourceForm(request.POST)
        if journalResourceForm.is_valid():
            journalResources = journalResourceForm.save(commit=False)
            journalResources.save()

    else :
        journalResourceForm = JournalResourceForm()


    template = loader.get_template('alljournalresources.html')
    context = {
        'journalResourceForm': journalResourceForm,
        'journalResources': journalResources,
    }
    return HttpResponse(template.render(context, request))




class ResourceView(generic.ListView):
    template_name = 'alljournalresources.html'
    context_object_name = 'journalResources'

    def get_queryset(self):
        """Return the last five published questions."""
        return JournalResource.objects.order_by('journalName')  #order_by('-pub_date')[:5]


class ResourceCreateView(CreateView):
    template_name = 'addResource.html'

    model = JournalResource
    fields = '__all__'

class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['name', 'url']

# class ResourceDeleteView(DeleteView):
#     model = Resource
#     success_url = reverse_lazy('Resource-list')