import discord
from discord import channel
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(912664191251415040)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(912664191251415040)
    await channel.send(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')

bot.run("OTEyNjY1NjE0NTU5MTE3Mzg1.YZzQFw.TyFDCLWs9Syb9NDme9mzf5cyavM")