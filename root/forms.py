from .models import *
from django import forms
class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = ['email']

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message']
class AppointmentsForm(forms.ModelForm):
    
    class Meta:
        model = Appointments
        fields = ['name','email','phone','date','department','doctor', 'message',]