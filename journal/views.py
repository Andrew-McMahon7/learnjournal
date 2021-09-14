from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import ContactsResource, JournalResource, Resource, TagsResource, ContactsResource
from django.template import loader
from django.template.loader import render_to_string
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from journal.forms import JournalResourceForm, TagResourceForm, ContactResourceForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    journalResources = JournalResource.objects.all().order_by('journalName')
    tagResources = TagsResource.objects.all().order_by('tagName')
    contactResources = ContactsResource.objects.all().order_by('contactName')
    orderedJResources = JournalResource.objects.all().order_by('lastAccessed').reverse()[:3]
    journalResourceForm = JournalResourceForm()

    if request.POST:
        journalResourceForm = JournalResourceForm(request.POST)
        if journalResourceForm.is_valid():
            journalResources = journalResourceForm.save(commit=False)
            journalResources.save()

    else :
        journalResourceForm = JournalResourceForm()


    template = loader.get_template('Homepage.html')
    context = {
        'journalResourceForm': journalResourceForm,
        'journalResources': journalResources,
        'tagResources': tagResources,
        'contactResources': contactResources,
        'orderedJResources': orderedJResources,
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
    success_url = reverse_lazy('resources')

    Resource_Name = 'Journal Resource'

    model = JournalResource
    form_class = JournalResourceForm

    def get_context_data(self, **kwargs):
        context = super(ResourceCreateView, self).get_context_data(**kwargs)
        context['resource_type'] = self.Resource_Name
        return context



class TagCreateView(CreateView):
    template_name = 'addResource.html'
    success_url = reverse_lazy('resources_tags')

    Resource_Name = 'Software Tag'

    model = TagsResource
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['resource_type'] = self.Resource_Name
        return context


class ContactCreateView(CreateView):
    template_name = "addResource.html"
    success_url = reverse_lazy("resources_contacts")

    Resource_Name = 'Contact'

    model = ContactsResource
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['resource_type'] = self.Resource_Name
        return context

class ResourceUpdateView(UpdateView):
    model = JournalResource
    form_class = JournalResourceForm
    template_name = 'updateResource.html'
    success_url = reverse_lazy('resources')


class ContactUpdateView(UpdateView):
    model = ContactsResource
    fields = '__all__'
    template_name = 'updateResource.html'
    success_url = reverse_lazy('resources_contacts')
# class ResourceDeleteView(DeleteView):
#     model = Resource
#     success_url = reverse_lazy('Resource-list')

class TagUpdateView(UpdateView):
    model = TagsResource
    fields = '__all__'
    template_name = 'updateResource.html'
    success_url = reverse_lazy('resources_tags')

class ResourceDeleteView(DeleteView):
    model = JournalResource
    template_name = 'deleteResource.html'
    success_url = reverse_lazy('resources')

class TagDeleteView(DeleteView):
    model = TagsResource
    template_name = 'deleteTag.html'
    success_url = reverse_lazy('resources_tags')

class ContactDeleteView(DeleteView):
    model = ContactsResource
    template_name = 'deleteContact.html'
    success_url = reverse_lazy('resources_contacts')
