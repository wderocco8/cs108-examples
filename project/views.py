from django.db.models.query import QuerySet
from django.shortcuts import render
from project.models import Exercise, User, Schedule
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
class HomePageView(ListView):
    '''Displays home page of website'''
    model = Exercise                    # retrieve Exercise objects from the database
    template_name = "project/home.html" # delegate the display to this template
    context_object_name = "exercises"   # use this variable name in the template

class ShowAllExercisesView(ListView):
    '''Shows a list of all possible exercises to add to planner.'''
    model = Exercise                                  # retrieve Exercise objects from the database
    template_name = "project/show_all_exercises.html" # delegate the display to this template
    context_object_name = "exercises"                 # use this variable name in the template

class ShowAllUsersView(ListView):
    '''Shows a list of all current users'''
    model = User                                  # retrieve User objects from the database
    template_name = "project/show_all_users.html" # delegate the display to this template
    context_object_name = "users"                 # use this variable name in the template

class ShowUserPage(ListView):
    '''Shows a list of days of which user can select to choose exercises for each day.'''
    model = User
    template_name = "project/show_user_page.html"
    context_object_name = "user"

class CreateExerciseView(CreateView):
    '''Create a new Profile to store in the database.'''
    model = Exercise                                    # retrieve Exercise objects from the database
    form_class = CreateExerciseForm                     # which form to use to create Exercise
    template_name = "project/create_exercise_form.html" # delegate the display to this template

def add_exercise(request, user_pk, exercise_pk, schedule_pk):
    '''Process a form submission to add an exercise to a user's schedule.'''
    # print(request.POST) # for debugging at the console
    
    # identify user making the request
    user = User.objects.get(pk=user_pk)
    
    # identify exercise being requested
    exercise = Exercise.objects.get(pk=exercise_pk)
    
    schedule = Schedule.objects.get(pk=schedule_pk)

    # add friend to list of profile object's friends
    schedule.exercises.add(exercise)

    # associate user with related schedule
    schedule.user = user

    # save this modified profile
    schedule.save()
    
    # redirect the user to the show_profile_page view
    url = reverse('show_schedule_page', kwargs={'pk': user_pk})
    return redirect(url)


class ShowUserScheduleView(DetailView):
    '''Displays the one instance of a specific users exercises/schedule.'''


# class UpdateExerciseView(UpdateView):
#     '''Update a Profile to store in the database.'''
#     model = Exercise
#     form_class = UpdateExerciseForm
#     template_name = "project/update_exercise_form.html"

# class ShowScheduleView(ListView):
#     '''Shows a list of all current exercises for a specific user's schedule.'''
#     model = 