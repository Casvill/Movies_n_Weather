import requests
import json

#------------------------------------------------------------------------------------------------------------------------
def send_to_webhook(data: dict, webhook_url: str):
    """
    Sends the provided data to the specified webhook URL using a POST request.

    Parameters:
    -----------
    data : dict
        The data to send in the POST request (must be in dictionary format).
    webhook_url : str
        The URL of the webhook to send the data to.

    Returns:
    --------
    None
        Prints a message indicating whether the data was successfully sent or if there was an error.

    Example:
    --------
    >>> send_to_webhook({"message": "Hello, webhook!"}, "https://webhook.site/example")
    Data sent successfully to the webhook.
    """

    json_data = json.dumps(data)

    # Headers for the HTTP request
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Send data to the webhook using a POST request
        response = requests.post(webhook_url, data=json_data, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data sent successfully to the webhook.")
        else:
            print(f"Error sending data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Catch any exception raised by the requests library
        print(f"An error occurred while sending data: {e}")
#------------------------------------------------------------------------------------------------------------------------
