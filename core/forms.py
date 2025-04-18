from django import forms
from .models import CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'profile_photo',
            'membership_status',
            'membership_type',
            'phone',
            'position',
            'course',
            'year',
            'department'
        ]
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'membership_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'membership_type': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }