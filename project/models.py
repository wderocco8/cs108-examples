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

class User(models.Model):
    '''Represents a User involving first/last name , birthdate, weight, height, city, email, profile picture.'''
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



class Schedule(models.Model):
    '''Represents a Schedule which relates exercises and users while including weekday, start/end time, total time'''
    exercise = models.ManyToManyField("Exercise", blank=True) # allow any Schedule object to have various Exercise objects
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weekday = models.TextField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    # total_time = 

    def __str__(self):
        '''Return the string representation of Status Message.'''
        
        return f'{self.exercise} {self.user} {self.weekday}'