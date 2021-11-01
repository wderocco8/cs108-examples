# mini_fb/urls.py

from django.urls import path
from .views import ShowAllProfilesView # our view class defintion

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    
]