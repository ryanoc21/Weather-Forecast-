import requests
"""
This file contains the code for processing the data retrieved from the weather forecase api.
"""


def get_data(location, forecast_days):

    # Link to five-day forecast data and api key
    api_key = "8ca95f091435046e1eb62e88204b3d73"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"

    # Get the data from the api
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']

    # There are 8 collection points per 24 hours.
    # To get all the values, multiply forecast days by 8
    num_values = 8*forecast_days

    # To get the data up to the point specified
    filtered_data = filtered_data[:num_values]

    return filtered_data
