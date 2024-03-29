# File: project/views.py
# Name: William De Rocco (wderocco@bu.edu)
# Description: file to create all views


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
    model = Exercise                                  # retrieve Exercise objects from the database
    template_name = "project/home.html"               # delegate the display to this template
    context_object_name = "exercises"                 # use this variable name in the template

class ShowAllExercisesView(ListView):
    '''Shows a list of all possible exercises to add to planner.'''
    model = Exercise                                  # retrieve Exercise objects from the database
    template_name = "project/show_all_exercises.html" # delegate the display to this template
    context_object_name = "exercises"                 # use this variable name in the template

class ShowAllUsersView(ListView):
    '''Shows a list of all current users'''
    model = User                                     # retrieve User objects from the database
    template_name = "project/show_all_users.html"    # delegate the display to this template
    context_object_name = "users"                    # use this variable name in the template

class CreateUserView(CreateView):
    '''Create a new user to store in the database.'''
    model = User                                     # retrieve User objects from the database
    form_class = CreateUserForm                      # delegate the display to this template
    template_name = "project/create_user_form.html"  # use this variable name in the template
    
    def get_success_url(self):
        '''Provide a url to show this object to direct back to page showing all users.'''

        return reverse('all_users')


class ShowUserPageView(DetailView):
    '''Shows a list of days of which user can select to choose exercises for each day.'''
    model = User                                    # retrieve User objects from the database
    template_name = "project/show_user_page.html"   # delegate the display to this template
    context_object_name = "user"                    # use this variable name in the template

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the User record to display for this page view
        context = super(ShowUserPageView, self).get_context_data(**kwargs)
        # create a new CreateScheduleForm, and add it into the context dictionary
        form = CreateScheduleForm() 
        context['create_schedule_form'] = form
        # return this context dictionary
        return context

class ShowNewExerciseView(DetailView):
    '''Shows a new exercise that has just been added.'''
    model = Exercise                                    # retrieve Exercise objects from the database
    template_name = "project/show_new_exercise.html"    # delegate the display to this template
    context_object_name = "exercise"                    # use this variable name in the template

class CreateExerciseView(CreateView):
    '''Create a new Exercise to store in the database.'''
    model = Exercise                                    # retrieve Exercise objects from the database
    form_class = CreateExerciseForm                     # which form to use to create Exercise
    template_name = "project/create_exercise_form.html" # delegate the display to this template

    def get_success_url(self):
        '''Provide a url to direct back to a list of all exercises.'''

        return reverse('show_all_exercises')

class UpdateUserView(UpdateView):
    '''Update a User to store in the database.'''
    model = User                                       # retrieve User objects from the database
    form_class = UpdateUserForm                        # which form to use to update User
    template_name = "project/update_user_form.html"    # delegate the display to this template


class UpdateExerciseView(UpdateView):
    '''Update a USer to store in the database.'''
    model = Exercise                                    # retrieve Exercise objects from the database
    form_class = UpdateExerciseForm                     # which form to use to update User
    template_name = "project/update_exercise_form.html" # delegate the display to this template

def create_schedule(request, pk):
    '''
    Process a form submission to create a new Schedule.
    '''
    # print("create_schedule") --> debugging
    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateScheduleForm(request.POST or None, request.FILES or None) # files necessary for image
        # print(form) --> debugging
        if form.is_valid():
            print(form) # --> debuggin
            # create the Schedule object with the data in the CreateScheduleForm
            schedule = form.save(commit=False) # don't commit to database yet

            # find the user that matches the `pk` in the URL
            user = User.objects.get(pk=pk)

            # attach FK user to this schedule
            schedule.user = user

            # now commit to database
            schedule.save()

            # save form using many to many save method
            form.save_m2m()

    # redirect the user to the show_user_page view
    url = reverse('show_user_page', kwargs={'pk': pk})
    return redirect(url)


class UpdateScheduleView(UpdateView):
    '''Update a Schedule to store in the database.'''
    # model = Schedule
    # form_class = UpdateScheduleForm
    # template_name = "project/update_schedule_form.html"
    
    # obtain all schedule objects
    QuerySet = Schedule.objects.all()
    # identify form to submit to
    form_class = UpdateScheduleForm
    # identify template to redirect to
    template_name = "project/update_schedule_form.html"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the User record to display for this page view
        context = super(UpdateScheduleView, self).get_context_data(**kwargs)
        schedule = Schedule.objects.get(pk=self.kwargs['schedule_pk'])
        context['schedule'] = schedule
        # return this context dictionary
        return context

    def get_object(self):
        '''Return the schedule of an object that should be deleted'''
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']
        schedule_pk = self.kwargs['schedule_pk']

        schedule_update = Schedule.objects.get(pk=schedule_pk)

        # find the Schedule object, and return it        
        return schedule_update

    def get_success_url(self):
        '''Provide a URL for after a schedule is deleted'''
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']
        schedule_pk = self.kwargs['schedule_pk']


        # reverse to show the person page
        return reverse('show_user_page', kwargs={'pk':user_pk})



class DeleteScheduleView(DeleteView):
    '''View to delete a schedule.'''
    # get all schedule objects
    QuerySet = Schedule.objects.all()
    # identify template to submit to
    template_name = "project/delete_schedule_form.html"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the User record to display for this page view
        context = super(DeleteScheduleView, self).get_context_data(**kwargs)
        schedule = Schedule.objects.get(pk=self.kwargs['schedule_pk'])
        context['schedule'] = schedule
        # return this context dictionary
        return context

    def get_object(self):
        '''Return the schedule of an object that should be deleted'''
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']
        schedule_pk = self.kwargs['schedule_pk']

        schedule_kill = Schedule.objects.get(pk=schedule_pk)

        # find the Schedule object, and return it        
        return schedule_kill

    def get_success_url(self):
        '''Provide a URL for after a schedule is deleted'''
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']
        schedule_pk = self.kwargs['schedule_pk']


        # reverse to show the person page
        return reverse('show_user_page', kwargs={'pk':user_pk})
