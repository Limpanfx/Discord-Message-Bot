import requests

TOKEN = "YOUR_DISCORD_USER_TOKEN"  # Replace with your user token
CHANNEL_ID = "YOUR_CHANNEL_ID"  # Replace with the target channel ID
MESSAGE = "YOUR_MESSAGE"  # Customize your message
COOLDOWN = 10 # How often you want to send your message in seconds

while wait(COOLDOWN):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "content": MESSAGE
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.text}")
