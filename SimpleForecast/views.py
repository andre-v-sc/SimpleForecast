# Import render function and required libraries from Django
from django.shortcuts import render
import json
import requests

# Function to determine air quality category based on AQI value


def get_category_data(aqi):
    if aqi >= 0 and aqi <= 50:
        return 'good', 'Air quality is considered satisfactory, and air pollution poses little or no risk.'
    elif aqi >= 51 and aqi <= 100:
        return 'moderate', 'Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
    elif aqi >= 101 and aqi <= 150:
        return 'usg', 'Members of sensitive groups may experience health effects. The general public is not likely to be affected.'
    elif aqi >= 151 and aqi <= 200:
        return 'unhealthy', 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
    elif aqi >= 201 and aqi <= 300:
        return 'veryunhealthy', 'Health alert: everyone may experience more serious health effects.'
    elif aqi >= 301:
        return 'hazardous', 'Health warnings of emergency conditions. The entire population is more likely to be affected.'

    return None, None

# Home view function


def home(request):
    # Check if request method is POST
    if request.method == "POST":
        zip = request.POST['zip']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip + "&distance=30&API_KEY=2016116F-EA63-4ABC-ACA0-0EBB2C79EA16")
    else:
        # Default API request -- Cabrini
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19087&distance=30&API_KEY=2016116F-EA63-4ABC-ACA0-0EBB2C79EA16")
        zip = "19087"

    # Load API response into JSON format
    try:
        api = json.loads(api_request.content)
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

    # Render home.html with necessary context
    return render(request, 'home.html', {
        'api': api,
        'category_description': category_description,
        'category_color': category_color,
        'zip': zip
    })


# About view function

def about(request):
    return render(request, 'about.html', {})
