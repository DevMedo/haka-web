from django import forms
from .models import contactRequest


class contactForm(forms.ModelForm):
    class Meta:
        model = contactRequest
        fields = ['name', 'email']
