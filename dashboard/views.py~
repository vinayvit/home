from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from dashboard.models import Document, Event
from dashboard.forms import DocumentForm, EventForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from .models import Document, Event
#from myproject.myapp.models import Document
#from myproject.myapp.forms import DocumentForm
from .forms import DocumentForm, EventForm ,EvtForm


@login_required
def dashboard(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, "tag.html", {'document':document})

@login_required
def profiles(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, "profil.html", {'document':document})



def edit(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES )
        if form.is_valid():
            newdoc = Document(user=request.user, docfile = request.FILES['docfile'], firstname = request.POST['firstname'], lastname = request.POST['lastname'], address = request.POST['address'],)
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.profiles')
    else:
        form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
    document = Document.objects.filter(user_id = request.user.id)[:1]
   

    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/list.html',
        {'document': document, 'form': form},
        context_instance=RequestContext(request)
    )

def event(request):
    model = Event,User
    event = Event.objects.all()

    document = Document.objects.filter( user_id = request.user.id)[:1]

    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.event')
    else:
        form = EventForm() # A empty, unbound form
    
    event = Event.objects.all()
   # Load documents for the list page
    
    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/event.html',
        { 'event': event,'document':document,'form': form,},
        context_instance=RequestContext(request)
    )

def event_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    user_id=event.user.id
    document = Document.objects.filter( user_id=event.user.id)[:1]
    return render(request,  'dashboard/eventdetail.html', {'event': event ,'document':document})

@login_required
def devent(request):
    document = Document.objects.filter(user_id = request.user.id)[:1]
    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.devent_detail')
    else:
        form = EventForm() # A empty, unbound form

   # Load documents for the list page
    event = Event.objects.all()
   

    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/userevent.html',
        {'event': event,'document':document, 'form': form},
        context_instance=RequestContext(request)
    )



def profile_edit(request, pk):
    newdoc = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=newdoc )
        if form.is_valid():
            newdoc = Document(user=request.user, docfile = request.FILES['docfile'], firstname = request.POST['firstname'], lastname = request.POST['lastname'], address = request.POST['address'],)
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.profiles', pk=newdoc.pk)
    else:
        form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
    document = Document.objects.filter(user_id = request.user.id)
   

    # Render list page with the documents and the form
    return render_to_response(
        'dashboard/list.html',
        {'document': document, 'form': form},
        context_instance=RequestContext(request)
    )
@login_required
def devent_detail(request):
    model = Event,Document,User
    event = Event.objects.filter(user_id = request.user.id)
    document = Document.objects.filter(user_id = request.user.id)
    return render(request,  'dashboard/detail.html', {'event': event, 'document': document })

@login_required
def uevent_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    document = Document.objects.filter(user_id = request.user.id)
    return render(request,  'dashboard/ueventdetail.html', {'event': event,'document': document })

def devent_edit(request,pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    document = Document.objects.filter(user_id = request.user.id)[:1]
    
    # Handle file upload
    if request.method == 'POST':
        form = EvtForm(request.POST,request.FILES, instance=event )
        if form.is_valid():
            event.user = request.user
            event.save()

            # Redirect to the document list after POST
            return redirect('dashboard.views.devent_detail')
    else:
        form = EvtForm(instance=event) # A empty, unbound form

   # Load documents for the list page

   

    # Render list page with the documents and the form
    return render(request,
        'dashboard/userevent.html',{'document':document, 'form': form})
    
	
def new(request):
    model = Document, User
    document = Document.objects.filter(user_id = request.user.id)
    return render(request, 'dashboard/new.html', {'document': document})



