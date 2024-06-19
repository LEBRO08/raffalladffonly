import discord
import asyncio
import random
import os
from flask import Flask
from keep_alive import keep_alive


keep_alive()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

port = os.environ.get('PORT', 8080)  # Default to 8080 if PORT environment variable is not set

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

client = MyClient()

@client.event
async def on_message(self, message):
        if message.author.id == 1150448986264698980:
            print("Message from bot.")

            for embed in message.embeds:
                if "Raffle created" in embed.description:
                    for component in message.components:
                        for child in component.children:
                            if child.label == "Enter":
                                await asyncio.sleep(random.randint(5, 15))
                                await child.click()
                else:
                    print("Prize value is not more than $0.1, skipping entry.")

        elif "Airdrop created" in embed.description and message.guild.id == 1222623160734580736:
            for component in message.components:
                for child in component.children:
                    if child.label == "Enter":
                        await asyncio.sleep(random.randint(5, 10))
                        await child.click()

if __name__ == "__main__":
    client.run(os.environ['TOKEN'])