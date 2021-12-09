# File: project/urls.py
# Name: William De Rocco (wderocco@bu.edu)
# Description: file to create URL paths


from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('exercises', ShowAllExercisesView.as_view(), name="show_all_exercises"),
    path('create_user', CreateUserView.as_view(), name="create_user"),
    path('user/<int:pk>/update', UpdateUserView.as_view(), name="update_user"),
    path('create_exercise', CreateExerciseView.as_view(), name="create_exercise"),
    path('exercise/<int:pk>/update', UpdateExerciseView.as_view(), name="update_exercise"), 
    path('users', ShowAllUsersView.as_view(), name="all_users"),
    path('users/<int:pk>', ShowUserPageView.as_view(), name="show_user_page"),
    path('users/<int:pk>/create_schedule', create_schedule, name="create_schedule"),
    # path('schedule/<int:pk>/update', UpdateScheduleView.as_view(), name="update_schedule"),
    path('user/<int:user_pk>/update/<int:schedule_pk>', UpdateScheduleView.as_view(), name="update_schedule"),
    path('user/<int:user_pk>/delete_schedule/<int:schedule_pk>', DeleteScheduleView.as_view(), name="delete_schedule"),
    # path('schedule/<int:schedule_pk>/add_exercise/<int:exercise_pk>', add_exercise, name="add_exercise"),
]