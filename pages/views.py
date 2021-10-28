# file: pages/views.html
# description: provide a view to send to the user

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    '''A specialized version of TemplateView to display our home page.'''

    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    '''A specialized version of TemplateView to display our about page.'''

    template_name = "pages/about.html"

class SchedulePageView(TemplateView):
    '''A specialized version of TemplateView to display our schedule page.'''

    template_name = "pages/schedule.html"