import discord
import time
import numpy as np
from discord.ext import commands
import asyncio



intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def проблемы(ctx):
    await ctx.send('Причины глобального потепления:\n'
    '1.Выбросы парниковых газов:\n'
   'Решение: Переход на возобновляемые источники энергии,\n такие как солнечная и ветровая энергия, \nчтобы сократить зависимость от ископаемых и \nуменьшить выбросы парниковых газов.\n'
    '\n'
    '2.Загрязнение атмосферы:\n'
    'Решение: Использование чистых технологий \nи процессов производства, \nчтобы уменьшить выбросы вредных веществ в \nатмосферу и повысить качество воздуха.')
@bot.command()
async def помощь(ctx):
    await ctx.send('В проблеме с ГП вам помогут сайты:\n'
                   '1. https://www.un.org/ru/global-issues/climate-change \n'
                   '2. https://habr.com/ru/articles/560378/ ')
bot.run("YOUR_TOKEN")
