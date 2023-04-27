# Import render function and required libraries from Django
from django.shortcuts import render
import json
import requests
from django.core.cache import cache

# This function takes in an AQI value and returns the corresponding air quality category and description based on a defined dictionary of AQI ranges and their associated categories.
def get_category_data(aqi):
    categories = {
        (0, 50): ('good', 'Air quality is considered satisfactory, and air pollution poses little or no risk.'),
        (51, 100): ('moderate', 'Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'),
        (101, 150): ('usg', 'Members of sensitive groups may experience health effects. The general public is not likely to be affected.'),
        (151, 200): ('unhealthy', 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'),
        (201, 300): ('veryunhealthy', 'Health alert: everyone may experience more serious health effects.'),
        (301, float('inf')): ('hazardous', 'Health warnings of emergency conditions. The entire population is more likely to be affected.')
    }

    for range_, (category, message) in categories.items():
        if aqi >= range_[0] and aqi <= range_[1]:
            return category, message

    return None, None

# Home view function
def home(request, zip=None):
    if zip is None:
        # Use default zip code if none is provided
        zip = "19087"

    # Check if request method is POST
    if request.method == "POST":
        zip = request.POST['zip']

    api_key = "2016116F-EA63-4ABC-ACA0-0EBB2C79EA16"
    cache_key = f"api_request_{zip}"

    # Try to get cached API response
    api_request = cache.get(cache_key)

    if not api_request:
        # Make new API request if cache is expired or doesn't exist
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip}&distance=30&API_KEY={api_key}")
        # Cache API response for 5 minutes
        cache.set(cache_key, api_request, timeout=300)

    # Load API response into JSON format
    try:
        api = api_request.json()
    except Exception as e:
        api = None

    # Process API response if available and if not an error
    if api:
        aqi = api[0]['AQI']
        category_color, category_description = get_category_data(aqi)
        print("AQI:", aqi, "Color:", category_color,
              "Description:", category_description)
    else:
        category_color = "no-data"
        category_description = "No data available for the provided zip code."

    # Render home.html with necessary context variables
    return render(request, 'home.html', {
        'api': api,
        'category_description': category_description,
        'category_color': category_color,
        'zip': zip
    })

# About view function
def about(request):
    return render(request, 'about.html', {})