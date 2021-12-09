# File: project/forms.py
# Name: William De Rocco (wderocco@bu.edu)
# Description: file to create all forms


from django import forms
from .models import *

class CreateExerciseForm(forms.ModelForm):
    '''A form to create a Profile object.'''
    exercise_name = forms.CharField(label="Exercise Name", required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    instructions = forms.CharField(widget=forms.Textarea, required=True)
    image_url = forms.CharField(label="Image (or GIF) URL", required=True)    
    recommended_reps = forms.CharField(label="Reccomended Reps", required=True)
    muscle_groups = forms.CharField(label="Muscle Groups", required=True)


    class Meta:
        '''additional data about this form'''
        model = Exercise
        fields = ['exercise_name', 'description', 'instructions', 'image_url', 'recommended_reps', 'muscle_groups']


class UpdateExerciseForm(forms.ModelForm):
    '''A form to update a Exercise object.'''
    exercise_name = forms.CharField(label="Exercise Name", required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    instructions = forms.CharField(widget=forms.Textarea, required=True)
    image = forms.CharField(label="Image (or GIF) URL", required=True)
    recommended_reps = forms.CharField(label="Recommended Reps", required=True)
    muscle_groups = forms.CharField(label="Muscle Groups", required=True)

    class Meta:
        '''additional data about this form'''
        model = Exercise
        fields = ['exercise_name', 'description', 'instructions', 'image', 'recommended_reps', 'muscle_groups']


class CreateUserForm(forms.ModelForm):
    '''A form to create a User object.'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birthdate = forms.DateField(label="Birthdate", required=True)
    weight = forms.CharField(label="Weigth (lbs)", required=True)
    height = forms.CharField(label="Height (ft, in)", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    profile_picture = forms.URLField(label="Profile Picture URL", required=True)

    class Meta:
        '''additional data about this form'''
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'weight', 'height', 'city', 'email', 'profile_picture']

class UpdateUserForm(forms.ModelForm):
    '''A form to update a Profile object.'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    weight = forms.CharField(label="Weight (lbs)", required=True)
    height = forms.CharField(label="Height (ft, in)", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email Address (or n/a)", required=True)
    profile_picture = forms.CharField(label="Profile Picture URL", required=True)    

    class Meta:
        '''additional data about this form'''
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'weight', 'height', 'city', 'email', 'profile_picture']

class CreateScheduleForm(forms.ModelForm):
    '''A form to create a Schedule object.'''
    # create a list of weekdays which can be accessed using a forms.ChoiceField and associated with the attribute 'weekday'
    weekday_choices= [
    ('SU', 'Sunday'),
    ('MO','Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday')
    ]
    weekday = forms.ChoiceField(choices = weekday_choices)
    # weekday=forms.CharField(label='Select day of week:')
    # widget=forms.Select(choices=weekday_choices)

    start_time = forms.TimeField()
    end_time = forms.TimeField()
    exercise = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        '''Additional data about this form'''
        model = Schedule
        fields = ['weekday', 'exercise', 'start_time', 'end_time']

class UpdateScheduleForm(forms.ModelForm):
    '''A form to update a Profile object.'''
    # create a list of weekdays which can be accessed using a forms.ChoiceField and associated with the attribute 'weekday'
    weekday_choices= [
    ('SU', 'Sunday'),
    ('MO','Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday')
    ]
    weekday = forms.ChoiceField(choices = weekday_choices)
    # weekday=forms.CharField(label='Select day of week:')
    # widget=forms.Select(choices=weekday_choices)

    start_time = forms.TimeField()
    end_time = forms.TimeField()
        
    class Meta:
        '''Additional data about this form'''
        model = Schedule
        fields = ['weekday', 'exercise', 'start_time', 'end_time']