from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event


# Create your views here.

def index(request):
    return render(request, 'clubapp/index.html')

def getResource(request):
    resource_list = Resource.objects.all()
    context = {'resource_list' : resource_list}
    return render(request, 'clubapp/resource.html', context = context)

def getMeeting(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'clubapp/meeting.html', context = {'meeting_list' : meeting_list})

def meetingDetail(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    location = Meeting.location
    context = {
        'meet' : meet,
        'location' : location,
    }
    return render(request, 'clubapp/meetingdetail.html', context = context)