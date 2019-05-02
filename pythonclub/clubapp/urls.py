from django.urls import path
from . import views

#takes proj urls include and transfers it to the views render request
urlpatterns=[
    path('', views.index, name='index'),
    path('getResource', views.getResource, name='resource'),
    path('getMeeting', views.getMeeting, name='meeting'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='meetingdetail'),
]
