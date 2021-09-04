import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive
import requests
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix='?', intents=intents)

#this simply prints when the bot is online on the console
@client.event
async def on_ready():
    print('We are online now with {0.user}'.format(client))


#this sends a direct message to the person joining a server containing this bot
@client.event
async def on_member_join(member: discord.Member):
  channel = await member.create_dm()
  await channel.send(f'Hi {member.name}, welcome to my Discord server!')

# @client.event
# async def on_member_remove(ctx, member):
#    await ctx.send(f'{member} has left the server!')

# clear <number> lets the user delete messages easily
@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

#this makes the bot respond with a random quote when user uses the command ?get_quote using an api
@client.command()
async def get_quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(quote)

# this makes the bot respond with the quote of the day when user types in ?qotd using an api
@client.command()
async def qotd(ctx):
    response = requests.get("https://zenquotes.io/api/today")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    await ctx.send(quote)

# this command makes the bot reply with a random quote from the show The Office by using an api
@client.command()
async def office_quote(ctx):
    response = requests.get("https://officeapi.dev/api/quotes/random")
    json_data = json.loads(response.text)
    quotes = json_data['data']['content'] + " - " + json_data["data"]['character']['firstname'] + " " + json_data["data"]['character']['lastname']
    await ctx.send(quotes)

# this command makes the bot reply with a random quote from the show Brooklyn99 by using an api
@client.command()
async def b99_quote(ctx):

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'DADDYYY',
        'Cool cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.'
    ]
    
    await ctx.send(random.choice(brooklyn_99_quotes))

# One of the first commands made for this bot, this command lets the user know that the bot online and working.
@client.command()
async def botstatus(ctx):
    await ctx.send(
        "If you recieved a response the bot is running just fine.")

# this commands rolls a dice 
@client.command()
async def dice(ctx):
    variable = ['one', 'two', 'three', 'four', 'five', 'six']
    await ctx.send(random.choice(variable))

# this command gives a random reply when asked a question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain',
        'It is decidedly so', 
        'Without a doubt',
        'Yes, definitely',
        'You may rely on it', 
        'As I see it, yes',
        'Most likely', 
        'Outlook good', 
        'Yes', 
        'Signs point to yes'
        'Reply hazy try again', 
        'Ask again later', 
        'Better not tell you now',
        'Cannot predict now', 
        'Concentrate and ask again', 
        "Don't count on it",
        'My reply is no', 
        'My sources say no', 
        'Outlook not so good',
        'Very doubtful'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# this command lets the user kick anyone in the server except the owner of the server with reasoning
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for {reason}')

# this commands informs the user about the bot
@client.command()
async def hello(ctx):
    await ctx.send("Hello, thanks for using this bot. You can add this bot to your server using https://bit.ly/anodiscordbot . To learn more about the commands the bot supports right now, type in ?commands")

# this command responds with a list of command the bot works with 
@client.command()
async def commands(ctx):
    await ctx.send("We got 14 commands right now. The prefix to these commands are ?. The list of commands includes: ?hello, ?commands, ?hi, ?get_quote, ?qotd, ?office_quote, ?b99_quote, ?botstatus, ?8ball, ?dice, ?kick, ?ping, ?ban and ?clear. ")

#this bot responds with a random response to the user's hi
@client.command()
async def hi(ctx):
    variable = [
      'Hello sir', 
      'WAASSSUP',
      'Bonjour!', 
      'supppp',
      'Hey! Getting bored? Try out ?commands for the list  of commands you can try', 
      'hi sir'
     ]    
    await ctx.send(random.choice(variable))


# can be used to check the user's ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# can be used to ban someone by the user
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason}')

# can be used to unban someone by the user
#@client.command()
#async def unban(ctx, *, member):
#    banned_users = await ctx.guild.bans()
#    member_name, member_discriminator = member.split('#')

#    for ban_entry in banned_users:
#        user = ban_entry.user

#        if(user.name, user.discriminator) == (member_name, member_discriminator):
#            await ctx.guild.unban(user)
#            await ctx.send(f'Unbanned {user.mention}')
#            return
       

keep_alive()
token = os.environ['Secret']
client.run(token)
