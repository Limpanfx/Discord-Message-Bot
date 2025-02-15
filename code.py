import requests
import time

TOKEN = "YOUR_DISCORD_USER_TOKEN"  # Replace with your user token
CHANNEL_ID = "YOUR_CHANNEL_ID"  # Replace with the target channel ID
MESSAGE = "YOUR_MESSAGE"  # Customize your message
COOLDOWN = 10 # How often you want to send your message in seconds

Counter = 0














print1 = """
██╗     ██╗███╗   ███╗██████╗  █████╗ ███╗   ██╗         ██████╗  ██████╗  █████╗ ████████╗
██║     ██║████╗ ████║██╔══██╗██╔══██╗████╗  ██║        ██╔════╝ ██╔═══██╗██╔══██╗╚══██╔══╝
██║     ██║██╔████╔██║██████╔╝███████║██╔██╗ ██║        ██║  ███╗██║   ██║███████║   ██║   
██║     ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██║╚██╗██║        ██║   ██║██║   ██║██╔══██║   ██║   
███████╗██║██║ ╚═╝ ██║██║     ██║  ██║██║ ╚████║        ╚██████╔╝╚██████╔╝██║  ██║   ██║   
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝         ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                                           """

print(print1)

while True:
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "content": MESSAGE
    }
    Counter = Counter + 1

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Message sent successfully! (" + str(Counter) + ")")
    else:
        print(f"Failed to send message: {response.text}")
    time.sleep(COOLDOWN)
