from django import forms
from .models import *

class CreateExerciseForm(forms.ModelForm):
    '''A form to create a Profile object.'''
    exercise_name = forms.CharField(label="Exercise Name", required=True)
    description = forms.CharField(label="Description", required=True)
    instructions = forms.CharField(label="Instructions", required=True)
    image_url = forms.CharField(label="Image URL", required=True)    
    recommended_reps = forms.CharField(label="Reccomended Reps", required=True)
    muscle_groups = forms.CharField(label="Muscle Groups", required=True)


    class Meta:
        '''additional data about this form'''
        model = Exercise
        fields = ['exercise_name', 'description', 'instructions', 'image_url', 'recommended_reps', 'muscle_groups']


# class UpdateProfileForm(forms.ModelForm):
#     '''A form to update a Profile object.'''
#     city = forms.CharField(label="City", required=True)
#     email_address = forms.CharField(label="Email Address", required=True)
#     image_url = forms.CharField(label="Image URL", required=True)    
#     birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

#     class Meta:
#         '''additional data about this form'''
#         model = Profile
#         fields = ['birth_date', 'city', 'email_address', 'image_url']

# class CreateStatusMessageForm(forms.ModelForm):
#     '''A form to create Status Message for Profile object.'''
#     # timestamp = forms.DateTimeField()
#     image = forms.ImageField(label="Image File", required=False)

#     class Meta:
#         '''additional data about this form'''
#         model = StatusMessage
#         fields = ['message', 'image', 'profile']