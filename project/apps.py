# File: project/apps.py
# Name: William De Rocco (wderocco@bu.edu)
# Description: file to configure app


from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
