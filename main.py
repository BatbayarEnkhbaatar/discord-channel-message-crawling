import json
import discord
import datetime as dt
# logging.basicConfig(level=logging.INFO)
client = discord.Client(intents=discord.Intents.default())
guild = discord.Guild
token = 'MTAzMjg0MjE1NTgzNzg5NDgxNg.GG1mpa.G4J3t56nykQskxkCaSIrf0g7Hls0dpJfax6aaQ'
channel_id = '1034280007729676311'
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    after_date = dt.datetime.utcnow() - dt.timedelta(days=2)
    before_date = dt.datetime.utcnow() - dt.timedelta(days=1)
    channel = client.get_channel(1034280007729676311)
    messages = [message async for message in channel.history(limit=123, oldest_first=True, after=after_date, before=before_date)]
    cont = []
    for message in messages:
        print("DATE: ", message.created_at)
        print("USER: ",message.author)
        print("CONTENT: ", message.content)
        cont.append(
            {
                'DATE': message.created_at,
                'USER': message.author,
                'CONTENT': message.content
            }
        )
        # result = json.dumps(cont, indent=2, default=str)
        with open("messages.json","w") as file:
            # file.truncate()
            json.dump(cont, file, default=str, indent=2)
    print("it's done")


client.run(token)

