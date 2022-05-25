import os
import disnake
from disnake.ext import commands,tasks

from alive import live

token = os.environ["key"]

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="-",intents=intents)

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  
@bot.command()
async def hello(ctx):
  await ctx.send("Hello there!")

live()
bot.run(token)
