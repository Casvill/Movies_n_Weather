# Movie Weather Application

This application allows users to search for a movie by title and retrieve information about the movie's official title, genre(s), and release date. Additionally, it fetches weather conditions (min and max temperature) on the movie's release date based on specified latitude and longitude coordinates, defaulting to the coordinates of Manizales, Colombia, if not provided. The combined data is then sent to a specified webhook for further processing. (You can see it [here](https://webhook.site/#!/view/d5d3bffd-4e65-4017-9b6f-6ef344ec0980/7aa737e6-17a8-4e09-8078-158882beadb0/1))

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
- `pandas` library
- `retry_requests` library

You can install the required libraries using pip:

```bash
pip install requests pandas retry_requests
```

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/Casvill/Movies_n_Weather.git
cd .\Movies_n_Weather\
```
Install the required dependencies (as mentioned above).

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
