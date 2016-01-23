from django import forms
from django.contrib.auth.models import User
from products.models import Product, Service
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity','address', 'zip_Code', 'expire_date', )


class Service1Form(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('title', 'description', 'active', 'duraction', 'address', 'zip_Code', 'expire_date', )


class DocumentForm(forms.Form):
    
    title = forms.CharField(
        label='Item Title', widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )
    
    description = forms.CharField(
        label='Item Description', widget=forms.TextInput(attrs={'placeholder': 'Tell more about your donating item'})
    )   
   
    quantity = forms.IntegerField(
        label='Item Quantity', widget=forms.TextInput(attrs={'placeholder': 'No. of items you donating'})
    )
    zip_Code = forms.CharField(
        label='Your Zipcode', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )
    docfile = forms.FileField(
        label='Select  Your Product Image '
    )
    address = forms.CharField(
        label='Place Where Available', widget=forms.TextInput(attrs={'placeholder': 'Your loaction where item available '})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )

class ServiceForm(forms.Form): 
	
    title = forms.CharField(
        label='Service Title', widget=forms.TextInput(attrs={'placeholder': 'Provide service name'})
    )
    
    description = forms.CharField(
        label='Service Description', widget=forms.TextInput(attrs={'placeholder': 'Some details about your service'})
    )  
    
    duraction = forms.CharField(
        label='Service Duration', widget=forms.TextInput(attrs={'placeholder': 'Time  schedule of service'})
    )
    zip_Code = forms.CharField(
        label='Your Zipcode',widget=forms.TextInput(attrs={'placeholder': 'Your area zipcode'})
    )
    docfile = forms.FileField(
        label='Select  Your Product Image'
    )
    address = forms.CharField(
        label='Place', widget=forms.TextInput(attrs={'placeholder': 'place where service offer'})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish '
    )
   



    
    
    
