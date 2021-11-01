from django.shortcuts import render
from mini_fb.models import Profile
from django.views.generic import ListView



# Create your views here.
class ShowAllProfilesView(ListView):
    '''Show a listing of Quotes.'''
    model = Profile # retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"