# forms.py
from django import forms
from .models import *


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']

class NoteForm(forms.ModelForm):
    class Meta:
        model = BookNote
        fields = ['note']