SimpleForecast

This web app provides real-time air quality information based on the Air Quality Index (AQI) for a given zip code. The app utilizes the AirNow API to fetch the AQI data and displays the information to users, along with a description of the air quality.

Features

Check real-time AQI for a specific zip code.
Get air quality category and health risk information based on the AQI value.
Responsive design for use on various devices.

Installation

Clone the repository.
Set up a virtual environment and activate it.
Install the required packages with pip install -r requirements.txt.
Run the development server with python manage.py runserver (MAC/Linux) or python3 manage.py runserver (Windows).

Usage

Access the web app at http://localhost:8000/ in your browser.
Enter a zip code in the form field and click the search button to see the AQI and air quality category.
Click on the "About Us" link to learn more about the app and the AQI.

App Structure

home(request): The main view function that handles both GET and POST requests. It fetches the AQI data from the AirNow API and processes it based on the provided zip code. The processed data is then passed to the home.html template and rendered.
get_category_data(aqi): A helper function that returns the air quality category and description based on the AQI value.
about(request): A view function that renders the about.html template, providing information about the app and AQI.
Templates

home.html: The main template that displays the air quality information based on the provided zip code. It also contains a form for users to input a zip code.
about.html: A template that provides information about the app and the AQI.

Dependencies

Django: The main web framework used to build the web app.
Requests: A library used to make HTTP requests to the AirNow API.
API Key: Provided by AirNow.

The AirNow API key used in this project is a sample key. To obtain your own API key, please visit AirNow API.

Replace the sample API key in the following line with your own:
api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip + "&distance=30&API_KEY=YOUR_API_KEY")

The project draws inspiration from Udemy instructor Comdemy/John Elder, with several modifications compared to the original project. These modifications include changes to the views.py, base.html, and both view files, with the inclusion of additional front end styling utilizing Bootstrap components. It should be noted that I do not have ownership of the original code in which this project is inspired by.
