from django.shortcuts import render
from mini_fb.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CreateProfileForm, UpdateProfileForm



# Create your views here.
class ShowAllProfilesView(ListView):
    '''Show a listing of Profiles.'''
    model = Profile                                  # retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html" # delegate the display to this template
    context_object_name = "profiles"                 # use this variable name in the template

class ShowProfilePageView(DetailView):
    '''Show a detail view of one Profile.'''
    model = Profile                                  # retrieve Profile objects from the database
    template_name = "mini_fb/show_profile_page.html" # delegate the display to this template
    context_object_name = "profile"                  # use this variable name in the template

class CreateProfileView(CreateView):
    '''Create a new Profile to store in the database.'''
    model = Profile                                    # retrieve Profile objects from the database
    form_class = CreateProfileForm                     # which form to use to create Profile
    template_name = "mini_fb/create_profile_form.html" # delegate the display to this template

class UpdateProfileView(UpdateView):
    '''Update a Profile to store in the database.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"