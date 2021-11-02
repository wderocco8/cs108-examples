# quotes/urls.py

from django.urls import path
from .views import * #HomePageView, QuotePageView, RandomQuotePageView, PersonPageView # our view class defintion

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name="random"),
    path('all', HomePageView.as_view(), name="all_quotes"),
    path('quote/<int:pk>', QuotePageView.as_view(), name="quote"),
    path('person/<int:pk>', PersonPageView.as_view(), name="person"),


]