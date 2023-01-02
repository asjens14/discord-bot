import discord
import os
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
token = os.getenv('TOKEN')



@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))


bot.run(token)