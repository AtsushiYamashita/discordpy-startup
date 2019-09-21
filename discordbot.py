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
    

async def logmsg(msg:Message):
    return await msg.content
    
@bot.command()
async def logrp(ctx, arg1: int):
    msgs = await ctx.message.channel.history(limit=arg1).flatten()    
    msg = ",".join(map(str,map(logmsg, msgs)))
    await ctx.send(msg)

bot.run(token)
