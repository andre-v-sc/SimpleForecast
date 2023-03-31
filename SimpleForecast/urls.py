# Import path function and view from Django

from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [
# Map the root URL to the home view in views.py
    path('', views.home, name="home"),
# Map the 'About' URL to the about view in views.py
    path('about.html', views.about, name="about"),
]