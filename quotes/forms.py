# forms.py

from django import forms
from .models import Image, Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to create a new Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to create
        fields = ['text', 'person'] # which field to create


class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to update
        fields = ['text', 'person'] # which field to update


class AddImageForm(forms.ModelForm):
    '''A form to collect an image from the user.'''
    
    class Meta:
        model = Image
        fields = ["image_file"]