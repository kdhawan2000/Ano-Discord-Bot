import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive
import requests
import json


client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
  print('We are online now with the bot account called {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

@client.command()
async def commands(ctx):
  await ctx.send ("We got 7 commands right now. This includes ?commands, ?dice, ?hello, ?hi, ?kick, ?botstatus and ?clear. ")

@client.command()
async def botstatus(ctx):
  await ctx.send ("This bot shouldnt get offline if Fusion turns off his laptop too.")

@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def dice(ctx):
  variable = {
    'one',
    'two',
    'three',
    'four',
    'five',
    'six'
  }
  await ctx.send({random.choice(variable)})

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for {reason}')

@client.command()
async def hello(ctx):
  await ctx.send ("bhak yaar kitni baar hello bologe.")

@client.command()
async def hi(ctx):
  variable = {
    'Hello noob',
    'chutta nahi hai',
    'mujhe bolna hi nahi hai im not interested yet',
    'supppp',
    'get a job instead of talking to a bot',
    'hi sir'
  }
  await ctx.send({random.choice(variable)})

keep_alive()
token = os.environ['Raaz']
client.run(token)
