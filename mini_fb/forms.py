from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a Profile object.'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email Address", required=True)
    image_url = forms.CharField(label="Image URL", required=True)    
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

    class Meta:
        '''additional data about this form'''
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_address', 'image_url']


class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile object.'''
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email Address", required=True)
    image_url = forms.CharField(label="Image URL", required=True)    
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

    class Meta:
        '''additional data about this form'''
        model = Profile
        fields = ['birth_date', 'city', 'email_address', 'image_url']

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create Status Message for Profile object.'''
    timestamp = forms.DateTimeField()

    class Meta:
        '''additional data about this form'''
        model = StatusMessage
        fields = ['timestamp', 'message', 'profile']