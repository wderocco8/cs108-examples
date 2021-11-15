from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    '''Represents profile involving name, hometown, and a profile pic'''

    # data attributes:
    # name = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of profile.'''

        return f'{self.first_name} {self.last_name} {self.city} {self.email_address} {self.image_url}'

    def get_status_messages(self):
        '''Obtain status messages for a Profile.'''

        # use the object manager to filter messages by this profile's pk:
        return StatusMessage.objects.filter(profile=self)


    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})


class StatusMessage(models.Model):
    '''Model the data attributes of Facebook status message.'''

    # data attributes:
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        '''Return the string representation of Status Message.'''
        # if self.image:
        #     return self.image.url

        # else:
        return f'{self.timestamp} {self.message} {self.image}'