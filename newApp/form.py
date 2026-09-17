
from django import forms

from newApp.models import menu


class foodForm(forms.ModelForm):
    class Meta:
        model = menu
        fields=['name','quantity','price','category']