from search_movie import search_movie
from send_to_webhook import send_to_webhook
from decouple import config

WEBHOOK_URL = config('WEBHOOK_URL')


#------------------------------------------------------------------------------------------------------------------------
def main():
    
    # Prompt user for the movie title
    query = input("Please write the movie title: ")

    # Get the webhook URL from the environment variable
    webhook_url = WEBHOOK_URL
    
    # Search for the movie and retrieve the relevant information
    movies_info = search_movie(query)

    # Send the gathered movie information to the specified webhook
    send_to_webhook(movies_info, webhook_url)
    
#------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()