from django import forms
from core.models import Event, Testimony

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'cover_p','date', 'location', 'description', 'attendees']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'cover_p': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'title', 'content', 'email', 'phone', 'cover_p']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'testimony'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'mobile number'}),
            'cover_p': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        }