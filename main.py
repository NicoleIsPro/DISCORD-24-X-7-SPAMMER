from webserver import keep_alive
import requests

channelID = 977487257239977994
headers = {
    "authorization":
    ""NzQzMTAxMzkxMTc3OTA4MzA0.YmjfjA.gEF2Xf-ZJ_sZQ9DAn448ViOQ9Fc""
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
