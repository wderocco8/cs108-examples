from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    '''Represents profile involving name, hometown, and a profile pic'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self", blank=True) # allow any Profile object to have other Profile objects as friends

    def __str__(self):
        '''Return a string representation of profile.'''

        return f'{self.first_name} {self.last_name}'

    def get_status_messages(self):
        '''Obtain status messages for a Profile.'''

        # use the object manager to filter messages by this profile's pk:
        return StatusMessage.objects.filter(profile=self)


    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})

    def get_friends(self):
        '''Returns all the friends for a Profile.'''
        
        return self.friends.all()

    def get_news_feed(self):
        '''Obtain and return list of news feed items.'''
        # news = StatusMessage.objects.all().order_by("-timestamp")
        news = StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")

        return news

class StatusMessage(models.Model):
    '''Model the data attributes of Facebook status message.'''

    # data attributes:
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        '''Return the string representation of Status Message.'''
        
        return f'{self.timestamp} {self.message} {self.image}'