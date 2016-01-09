from django import forms
from django.contrib.auth.models import User
from dashboard.models import Document ,Event
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    firstname = forms.CharField(
        label='Enter your first name',
    )
    lastname = forms.CharField(
        label='Enter your last name',
    )
    address = forms.CharField(
        label='Enter your address',
    )

class EventForm(forms.Form):
    eventtype = forms.CharField(required=False,label='Enter your Event Title name')
    snap = forms.FileField(required=False,label='Give the Event Look-up Picture ')
    
    date_event = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))    
    description = forms.CharField(label='Enter Event Description')
    place = forms.CharField(
        label='Enter Event Place',
    )
    dresscode = forms.BooleanField(
        label='Enter your Event Dress',
    )
    duration = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))  

class EvtForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('eventtype', 'snap', 'date_event', 'description','place', 'dresscode', 'duration', )
  
    
    
