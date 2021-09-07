from django.http.response import HttpResponse
from django.shortcuts import render
from journal.models import Resource
from django.template import loader

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