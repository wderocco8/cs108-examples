from django.db import models

# Create your models here.
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db.models.deletion import CASCADE

class Exercise(models.Model):
    '''Represents an Exercise involving description, instructions, time, image, reps, muscle group.'''

    # data attributes:
    exercise_name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    image = models.URLField(blank=True)
    recommended_reps = models.TextField(blank=True)
    muscle_groups = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of exercise.'''

        return f'{self.exercise_name}'

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_all_exercises')


class User(models.Model):
    '''Represents a User involving first/last name, birthdate, weight, height, city, email, profile picture.'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    weight = models.TextField(blank=True)
    height = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of exercise.'''

        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        # return reverse('show_all_users')
        return reverse('show_user_page', kwargs={'pk':self.pk})

    def get_schedule(self):
        'Retreive schedule items for user'

        # use the object manager to filter schedule by this profile's pk:
        return Schedule.objects.filter(user=self)




class Schedule(models.Model):
    '''Represents a Schedule which relates exercises and users while including weekday, start/end time, total time'''
    exercise = models.ManyToManyField("Exercise", blank=True) # allow any Schedule object to have various Exercise objects
    user = models.ForeignKey(User, on_delete=models.CASCADE) # each schedule is associated with one User object.
    # create a list of weekdays which can be accessed using a forms.ChoiceField and associated with the attribute 'weekday'
    SUNDAY = 'SU'
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    weekday_choices = [
        (SUNDAY, 'Sunday'),
        (MONDAY,'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday')
    ]
    weekday = models.CharField(
        max_length=2,
        choices=weekday_choices, 
        default=SUNDAY,
    )
    start_time = models.TimeField()
    end_time = models.TimeField() 

    def __str__(self):
        '''Return the string representation of user and weekday.'''
        
        return f'{self.user} {self.weekday}'

    def get_absolute_url(self):
        '''Provide a url to show this object which will redirect to showing all users page.'''

        # return reverse('show_all_users')
        return reverse('show_user_page', kwargs={'pk':self.pk})

    def get_exercises(self):
        '''Returns all the exercises for a Schedule.'''
        
        return self.exercise.all()