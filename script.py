import requests
import json

# The destination URL provided by the external service
webhook_url = "https://example.com"

# The data payload you want to send, formatted as a dictionary
payload = {
    "event": "user_signup",
    "user_id": 98765,
    "email": "user@example.com",
    "status": "active"
}

# Send the HTTP POST request with JSON data
try:
    response = requests.post(
        webhook_url, 
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status() 
    print("Webhook sent successfully.")
except requests.exceptions.RequestException as error:
    print(f"Failed to send webhook: {error}")
