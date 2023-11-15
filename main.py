import discord
import time
import numpy as np
from discord.ext import commands
import asyncio



intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def список(ctx):
    await ctx.send('Причины глобального потепления:\n'
    '1.')

bot.run("YOUR_TOKEN")
