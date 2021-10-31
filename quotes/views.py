from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote


class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Quote # retrieve Quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"