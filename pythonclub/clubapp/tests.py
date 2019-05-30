from django.test import TestCase
from django.urls import reverse
from .models import Meeting, MeetingMinute, Resource
from django.contrib.auth.models import User
import datetime
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        type = Meeting(titleid='1')
        self.assertEqual(str(type), type.titleid)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinuteTest(TestCase):
    def test_string(self):
        type = MeetingMinute(durationid='60')
        self.assertEqual(str(type), type.durationid)

    def test_table(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')


class ResourceTest(TestCase):
    def test_string(self):
        type = Resource(resourceid='W3')
        self.assertEqual(str(type), type.resourceid)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


#form Tests

class MeetingFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')

    def test_meetingForm(self):
        data={
            'titleid' : '1',
            'date' : datetime.datetime.now(),
            'time' : '12:47',
            'location' : 'seattle central',
            'agenda' : 'python',
        }
        form = MeetingForm(data=data)
        self.assertTrue(form.is_valid())