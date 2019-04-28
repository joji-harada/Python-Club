from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event


# Create your views here.

def index(request):
    return render(request, 'clubapp/index.html')

def getResource(request):
    resource_list = Resource.objects.all()
    context = {'resource_list' : resource_list}
    return render(request, 'clubapp/resource.html', context=context)