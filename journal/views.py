from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import ContactsResource, JournalResource, Resource, TagsResource, ContactsResource
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView 
from journal.forms import JournalResourceForm, TagResourceForm, ContactResourceForm

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


def resources_tags(request):
    tagResources = TagsResource.objects.all()
    TagResourceForm = TagResourceForm()

    if request.POST:
        TagResourceForm = TagResourceForm(request.POST)
        if TagResourceForm.is_valid():
            tagResources = TagResourceForm.save(commit=False)
            tagResources.save()

    else :
        TagResourceForm = TagResourceForm()


    template = loader.get_template('alltagsresources.html')
    context = {
        'TagResourceForm': TagResourceForm,
        'tagResources': tagResources,
    }
    return HttpResponse(template.render(context, request))

def resources_contacts(request):
    contactResources = ContactsResource.objects.all()
    ContactResourceForm = ContactResourceForm()

    if request.POST:
        ContactResourceForm = ContactResourceForm(request.POST)
        if ContactResourceForm.is_valid():
            contactResources = ContactResourceForm.save(commit=False)
            contactResources.save()

    else :
        ContactResourceForm = ContactResourceForm()


    template = loader.get_template('allcontactsresources.html')
    context = {
        'ContactResourceForm': ContactResourceForm,
        'contactResources': contactResources,
    }
    return HttpResponse(template.render(context, request))

class ResourceView(generic.ListView):
    template_name = 'alljournalresources.html'
    context_object_name = 'journalResources'

    def get_queryset(self):
        """Return the last five published questions."""
        return JournalResource.objects.order_by('journalName')  #order_by('-pub_date')[:5]

class TagResourceView(generic.ListView):
    template_name = 'alltagsresources.html'
    context_object_name = 'tagResources'

    def get_queryset(self):
        """Return the last five published questions."""
        return TagsResource.objects.order_by('tagName')  #order_by('-pub_date')[:5]


class ContactResourceView(generic.ListView):
    template_name = 'allcontactsresources.html'
    context_object_name = 'contactResources'

    def get_queryset(self):
        """Return the last five published questions."""
        return ContactsResource.objects.order_by('contactName')  #order_by('-pub_date')[:5]



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