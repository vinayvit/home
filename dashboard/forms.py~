from django import forms
from django.contrib.auth.models import User
from dashboard.models import Document ,Event
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Upload Your Profile Image'
    )
    firstname = forms.CharField(
        label='Your First Name', widget=forms.TextInput(attrs={'placeholder': 'Your first name'})
    )
    lastname = forms.CharField(
        label='Your Last Name', widget=forms.TextInput(attrs={'placeholder': 'Your surname'})
    )
    address = forms.CharField(
        label='Your Place', widget=forms.TextInput(attrs={'placeholder': 'Your loaction'})
    )

class EventForm(forms.Form):
    eventtype = forms.CharField(required=False,label='Event Title Name', widget=forms.TextInput(attrs={'placeholder': 'Title of event'}))
    snap = forms.FileField(required=False,label='Give the Event Look-up Picture ')
    
    date_event = forms.DateTimeField(label='Event Date',widget=DateTimeWidget(usel10n=True, bootstrap_version=3))    
    description = forms.CharField(label='Event Description', widget=forms.TextInput(attrs={'placeholder': 'Give some overview of your event'}))
    place = forms.CharField(
        label='Event Place', widget=forms.TextInput(attrs={'placeholder': 'Location of your event offer '})
    )    
    duration = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
    dresscode = forms.BooleanField(
        label='Event Dress Code Allow'
    )  

class EvtForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('eventtype', 'snap', 'date_event', 'description','place', 'dresscode', 'duration', )
  
    
    
