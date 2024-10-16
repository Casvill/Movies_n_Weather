import requests
import json
import pandas as pd
from retry_requests import retry

#------------------------------------------------------------------------------------------------------------------------
# Function to get the genre list and map it at its names
def get_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZjJmZTEyYjZhN2FmOTYxMmEyZmMzM2JmNjdkZWMwZSIsIm5iZiI6MTcyOTEwNDU2My4xMDcyNzEsInN1YiI6IjY3MTAwNzNlMWI5MTJhZGQyZWRiODhkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.33riMqWyy-mt8z92JQIn6TuAqAXAYiGYLE3fM-t0u0Q"
    }
    
    response = requests.get(url, headers=headers)
    genres_data = response.json()
    
    # Create a dict of genre_id -> genre_name
    genres_dict = {genre['id']: genre['name'] for genre in genres_data['genres']}
    
    return genres_dict

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
def weather_info(date, latitude=5.0689, longitude=-75.5174):
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

    # Make the request to the API
    response = requests.get(url, params=params)

    # Convert the response to JSON
    data = response.json()

    # Get max and min temperatures
    daily = data['daily']
    temperature_max = daily['temperature_2m_max'][0]
    temperature_min = daily['temperature_2m_min'][0]

    return temperature_max, temperature_min

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
# Function to search movies and show its details
def search_movies(query):
    url = f"https://api.themoviedb.org/3/search/movie?query={query}"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZjJmZTEyYjZhN2FmOTYxMmEyZmMzM2JmNjdkZWMwZSIsIm5iZiI6MTcyOTEwNDU2My4xMDcyNzEsInN1YiI6IjY3MTAwNzNlMWI5MTJhZGQyZWRiODhkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.33riMqWyy-mt8z92JQIn6TuAqAXAYiGYLE3fM-t0u0Q"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()

    # Get the genre dict (id -> name)
    genres_dict = get_genres()

    # List to store movie information
    movies_info = []

    # Verify if there are results
    if data["results"]:
        # Iterate over all results
        for movie in data["results"]:
            title = movie["original_title"]
            release_date = movie.get("release_date", "N/A")
            genre_ids = movie.get("genre_ids", [])
            
            # Get the names of the genres corresponding to the IDs
            genre_names = [genres_dict.get(genre_id, "Unknown") for genre_id in genre_ids]
            
            # Get weather information
            max_temp, min_temp = weather_info(release_date)
            
            # Store movie information in a dictionary
            movie_info = {
                "original_title": title,
                "release_date": release_date,
                "genres": genre_names,
                "max_temperature": max_temp,
                "min_temperature": min_temp
            }
            
            # Add the movie dictionary to the list
            movies_info.append(movie_info)

            # Print movie details
            print(f"Original Title: {title}")
            print(f"Release Date: {release_date}")
            print(f"Genres: {', '.join(genre_names)}")
            print(f"Weather Info: \n Max Temperature: {max_temp} \n Min Temperature: {min_temp}")
            print("-" * 40)  # Separator for each movie
        
        # Return the list of dictionaries with movie information
        return movies_info
    else:
        print("No results found.")
        return []
    
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
def send_to_webhook(movies_info, webhook_url):
    json_data = json.dumps(movies_info)

    # Headers for the HTTP request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send data to the webhook using a POST request
    response = requests.post(webhook_url, data=json_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Data sent successfully to the webhook.")
    else:
        print(f"Error sending data. Status code: {response.status_code}")
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
def main():
    # Main program code
    query = input("Please write the movie title:")
    webhook_url = "https://webhook.site/d5d3bffd-4e65-4017-9b6f-6ef344ec0980"
    movies_info = search_movies(query)

    send_to_webhook(movies_info, webhook_url)
#------------------------------------------------------------------------------------------------------------------------

# Check to ensure the file is run directly
if __name__ == "__main__":
    main()