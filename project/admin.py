# File: project/admin.py
# Name: William De Rocco (wderocco@bu.edu)
# Description: file to register modles to admin

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Exercise)
admin.site.register(User)
admin.site.register(Schedule)

