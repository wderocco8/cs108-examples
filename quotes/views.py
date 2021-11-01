from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote


class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Quote                       # retrieve Quote objects from the database
    template_name = "quotes/home.html"  # delegate the display to this template
    context_object_name = "quotes"      # use this variable name in the template

class QuotePageView(DetailView):
    '''Display a single quote object.'''
    model = Quote                       # retrieve Quote objects from the database
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote"       # use this variable name in the template
