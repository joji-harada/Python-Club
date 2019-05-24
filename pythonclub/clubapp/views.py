from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required


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

#form views

@login_required
def newResource(request):
    form=ResourceForm
    if request.method == 'POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form' : form})

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method == 'POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form' : form})



def loginMessage(request):
    return render(request, 'clubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'clubapp/logoutmessage.html')