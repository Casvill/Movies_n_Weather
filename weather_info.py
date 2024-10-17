import requests

def weather_info(date: str, latitude: float = 5.0689, longitude: float = -75.5174):
    """
    Make a request to the Open-Meteo API to get the max and min temperature
    of a specific location (Manizales, Colombia by default) on a given date.

    Parameters:
    -----------
    date : str
        Date when you want to get the max and min temperature, in the format 'YYYY-MM-DD'.
    latitude : float, optional
        Latitude of the location (default is 5.0689 for Manizales, Colombia).
    longitude : float, optional
        Longitude of the location (default is -75.5174 for Manizales, Colombia).

    Returns:
    --------
    tuple
        A tuple containing:
        - temperature_max (float): The maximum temperature on the given date or None if not found.
        - temperature_min (float): The minimum temperature on the given date or None if not found.

    Example:
    --------
    >>> weather_info("2022-10-12")
    (18.8, 11.9)
    """

    # Parameters for the API
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": date,
        "end_date": date,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "GMT"
    }

    try:
        # Make the request to the API
        response = requests.get(url, params=params)

        # Convert the response to JSON
        data = response.json()

        # Check if 'daily' exists in the response
        if 'daily' in data and data['daily']:
            daily = data['daily']
            temperature_max = daily['temperature_2m_max'][0]
            temperature_min = daily['temperature_2m_min'][0]
            return temperature_max, temperature_min
        else:
            print(f"No weather data found for {date}. Returning None values.")
            return None, None
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None