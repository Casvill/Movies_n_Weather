# Movie Weather Application

This application allows users to search for a movie by title and retrieve information about the movie's official title, genre(s), and release date. Additionally, it fetches weather conditions (min and max temperatures) on the movie's release date based on specified latitude and longitude coordinates, defaulting to the coordinates of Manizales, Colombia, if not provided. The combined data is then sent to a specified webhook for further processing.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Search for movies using a title or key word.
- Retrieve movie details including official title, genres, and release date.
- Fetch weather data (max and min temperatures) for the release date of the movie.
- Send combined movie and weather data to a specified webhook.
- Simple console interface for interaction.

## Requirements

- Python 3.x
- `requests` library
- `python-decouple` library

You can install the required libraries using pip:

```bash
pip install requests python-decouple
```

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/Casvill/Movies_n_Weather.git
cd Movies_n_Weather
```
Install the required dependencies (as mentioned above).

## .env File
Make sure to modify the .env file included in the project with the following content:
```bash
WEBHOOK_URL = "https://webhook.site/example"
THE_MOVIE_DB_API_TOKEN = "Write your movie db api token here"

# Location for which you want to obtain the max and min temperatures
LATITUDE = 5.0689 
LONGITUDE = -75.5174
```

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

   ```bash
   python movies_n_weather.py
   ```

4. When prompted, enter the title of the movie you want to search for.

5. The application will display the movie details along with the weather information and send the combined data to the specified webhook.

## Contributing
Contributions are welcome! If you would like to contribute, please fork the repository and create a pull request.

## License
This project is licensed under the GNU General Public License - see the LICENSE file for details.
