import discord
from discord.ext import commands
import os,random
from sampah import sampah_anorganik, sampah_organik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'bot sudah login dengan nama {bot.user}')

@bot.command()
async def organik(ctx):
    await ctx.send('salah satu contoh sampah organik adalah')
    await ctx.send(sampah_organik())

@bot.command()
async def anorganik(ctx):
    await ctx.send('salah satu contoh sampah anorganik adalah')
    await ctx.send(sampah_anorganik())

bot.run("")
