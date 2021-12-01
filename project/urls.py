# project/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('exercises', ShowAllExercisesView.as_view(), name="show_all_exercises"),
    path('create_exercise', CreateExerciseView.as_view(), name="create_exercise"),
    path('users', ShowAllUsersView.as_view(), name="all_users"),
    path('users/<int:pk>', ShowUserPage.as_view(), name="show_user_page"),
    path('schedule/<int:schedule_pk>/add_exercise/<int:exercise_pk>', add_exercise, name="add_exercise"),
]