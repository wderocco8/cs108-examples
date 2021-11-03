from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Represents profile involving name, hometown, and a profile pic'''

    # data attributes:
    name = models.TextField(blank=True)
    # first_name = models.TextField(blank=True)
    # last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of profile.'''

        return f'{self.name} {self.city} {self.email_address} {self.image_url}'