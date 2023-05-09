import discord
from discord.ext import commands
from discord import app_commands
import os
import random

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix='!', intents=intents,help_command = help_command)



#!Commands
@bot.command(description="Offer up a lightsaber")
async def lightsaber(ctx):
    await ctx.send("This will make a fine addition to my collection!", file=discord.File("media/fine_addition.gif"))

@bot.command(description="Greet the General", name='hello-there')
async def hello_there(ctx):
    await ctx.send("General Kenobi!", file=discord.File("media/kenobi.gif"))    

@bot.command(description="You are a jedi")
async def jedi(ctx):
    num = random.randint(1,3)
    if num == 1:
        await ctx.send("Jedi scum")
    if num == 2:
        await ctx.send("I will deal with this Jedi slime myself")
    if num == 3:
        await ctx.send("Murderer? Is it murder to rid the galaxy of you Jedi filth?")

#app commands


@bot.tree.command(guild=discord.Object(id=1041507219541331978))
async def begin(interaction:discord.Interaction):
    await interaction.response.send_message("https://www.starwars.com/video/star-wars-episode-iv-a-new-hope-opening-crawl")

#Displays once bot is logged on
@bot.event
async def on_ready():
    print(f"Logged in as bot {bot.user}")
    await bot.tree.sync(guild=discord.Object(id=1041507219541331978))
    print('ready')

bot.run(token)