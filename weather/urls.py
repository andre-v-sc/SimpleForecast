# Importing necessary Django modules
from django.contrib import admin
from django.urls import path, include

# List of URL patterns that Django should use
urlpatterns = [
    # Path to the admin page using admin.site.urls
    path('admin/', admin.site.urls),
    # Includes the URLs of SimpleForecast application
    path('', include('SimpleForecast.urls')),
]