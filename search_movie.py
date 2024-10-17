import requests
from weather_info import weather_info
from decouple import config

LATITUDE = config('LATITUDE')
LONGITUDE = config('LONGITUDE')

THE_MOVIE_DB_API_TOKEN = config('THE_MOVIE_DB_API_TOKEN')

HEADERS = {
        "accept": "application/json",
        "Authorization": THE_MOVIE_DB_API_TOKEN
    }

#------------------------------------------------------------------------------------------------------------------------
# Function to get the genre list and map it at its names
def get_genres():
    """
    Fetches the list of genres from The Movie Database API and returns a dictionary mapping genre IDs to genre names.

    Returns:
    --------
    dict: 
        A dictionary where the keys are genre IDs and the values are genre names.

    Example:
    --------
    >>> get_genres()
    {28: 'Action', 12: 'Adventure', 16: 'Animation', ...}
    """

    url = "https://api.themoviedb.org/3/genre/movie/list"
    
    try:

        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Check if the request was successful (status code 200)
        genres_data = response.json()
        
        # Create a dict of genre_id -> genre_name
        genres_dict = {genre['id'] : genre['name'] for genre in genres_data['genres']}
        
        return genres_dict
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return {}

#------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------
# Function to search movies and show its details
def search_movie(query: str):
    """
    Searches for movies by title using The Movie Database API and fetches detailed information including weather data.

    Parameters:
    -----------
    query : str
        The title of the movie to search for.

    Returns:
    --------
    list
        A list of dictionaries, each containing information about a movie including:
        - original_title: The movie's original title.
        - release_date: The release date of the movie.
        - genres: A list of genre names associated with the movie.
        - max_temperature: The maximum temperature on the movie's release date.
        - min_temperature: The minimum temperature on the movie's release date.

    Example:
    --------
    >>> search_movie("Inception")
    [{'original_title': 'Inception', 'release_date': '2010-07-15', 'genres': ['Action', 'Science Fiction'], 
      'max_temperature': 18.5, 'min_temperature': 12.3}, ...]
    """

    url = f"https://api.themoviedb.org/3/search/movie?query={query}"

    try: 
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        # Get the genre dict (id -> name)
        genres_dict = get_genres()

        # List to store movie information
        movies_info = []

        # Verify if there are results
        if data.get("results"):

            # Iterate over all results
            for movie in data["results"]:
                title = movie["original_title"]
                release_date = movie.get("release_date", "N/A")
                genre_ids = movie.get("genre_ids", [])
                
                # Get the names of the genres corresponding to the IDs
                genre_names = [genres_dict.get(genre_id, "Unknown") for genre_id in genre_ids]
                
                # Get weather information
                max_temp, min_temp = weather_info(release_date,LATITUDE, LONGITUDE)

                # Handle None values
                if max_temp is None or min_temp is None:
                    print(f"Weather information not available for {release_date}.")
                    max_temp = "N/A"
                    min_temp = "N/A"
                
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
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print the HTTP error

    except Exception as err:
        print(f"An error occurred: {err}")  # Print any other errors
        
    return []  # Return an empty list in case of error
    
#------------------------------------------------------------------------------------------------------------------------