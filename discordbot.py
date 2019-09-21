from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def date(ctx):
    await ctx.send(datetime.date.today())    
    

@bot.command()
async def logrp(ctx, arg1: int):
    await ctx.send(ctx.message)
    

bot.run(token)
