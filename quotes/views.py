from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Person, Quote, Person
from .forms import CreateQuoteForm, UpdateQuoteForm
import random


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

class RandomQuotePageView(DetailView):
    '''Display a single quote object.'''
    model = Quote                       # retrieve Quote objects from the database
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote"       # use this variable name in the template

    def get_object(self):
        '''Select one quote at random for display in the quote.html template.'''

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()
        # selct on at random
        q = random.choice(quotes)        
        return q


class PersonPageView(DetailView):
    '''Display a single person object.'''
    model = Person                       # retrieve Person objects from the database
    template_name = "quotes/person.html" # delegate the display to this template
    context_object_name = "person"       # use this variable name in the template

class CreateQuoteView(CreateView):
    '''Create a new Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = CreateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the display to this template

class UpdateQuoteView(UpdateView):
    '''Update a Quote object and store it in the database.'''

    model = Quote # which model to Update
    form_class = UpdateQuoteForm # which form to use to update the Quote
    template_name = "quotes/update_quote_form.html" # delegate the display to this template


class DeleteQuoteView(DeleteView):
    '''Delete a Quote object and store it in the database.'''
    
    template_name = "quotes/delete_quote.html" # delegate the display to this template
    queryset = Quote.objects.all()
    # success_url = "../../all" # what to do after deleting a quote

    def get_success_url(self):
        '''Return a URL to which we should be directed after the delete.'''

        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() # get one object from queryset

        # find the person associated with this quote
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})
        # reverse to show the person page