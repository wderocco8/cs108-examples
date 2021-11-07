from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
import random

# Create your models here.
class Person(models.Model):
    '''Represents a person who said something notable.'''

    name = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this Person.'''
        return self.name

    def get_random_image(self):
        '''Return an image of the person, selected at random.'''

        # find all images for this person:
        images = Image.objects.filter(person=self)

        # select one at random to return
        return random.choice(images)

    def get_all_quotes(self):
        '''Return all quotes for this Person.'''

        # use the object manager to filter Quotes by this person's pk:
        return Quote.objects.filter(person=self)

    def get_all_images(self):
        '''Return all images for this Person.'''

        # use the object manager to filter Image by this person's pk:
        return Image.objects.filter(person=self)


class Quote(models.Model):
    '''Represents a quote by a famous person.'''

    # data attributes:
    text = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)   
    #author = models.TextField(blank=True)
    #image_url = models.URLField(blank=True)

    def __str__(self):
       '''Return a string representation of this quote.'''

       return f'"{self.text}" - {self.person}'

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        # 'quote/<int:pk>'
        return reverse('quote', kwargs={'pk':self.pk})


class Image(models.Model):
    '''Represent an image URL for a Person.'''

    image_url = models.URLField(blank=True)
    person = models.ForeignKey(Person, on_delete=CASCADE)

    def __str__(self):
        '''Return the image url of this Image.'''
        return self.image_url