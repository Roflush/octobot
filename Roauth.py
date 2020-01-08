
import os
import discord
import asyncio
import random
from discord import message 

from discord.ext import commands 


token = open("token.txt", "r").read()

''' 
    python 3.7 or greater
    Discordpy 1.3 or greater 

'''
# Change the prefix below, and description to whatever you want.. 

bot = commands.Bot(command_prefix='ro.', description="This is a octobot, without all the bullshit the others carry.")

@bot.event # What you see in the cli.. 
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

@bot.command() # Adds two numbers (like this "/add 4 4",not like this "/add 4 + 4")
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command() # Subtracts two numbers (like this "/subu 4 4". not like this "/subu 4 - 4")
async def subu(ctx, left: int, right: int):
    '''Subtracts two numbers'''
    await ctx.send(left - right)

@bot.command() # Multiplies two numbers (like this "/mx 4 4",not like this "/mx 4 * 4")
async def mx(ctx, left: int, right: int):
    '''Multiplies two numbers'''
    await ctx.send(left * right)

@bot.command() # Divides two numbers (like this "/divide 4 4", not like this "/divide 4 / 4")
async def divi(ctx, left: int, right: int):
    '''Divides two numders.'''
    await ctx.send(left / right)

@bot.command() # Rolls a dice needs to be like this "/roll 1d4" the 1 is times rolled, and the 4 is sides.. 
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way') # Chooses two choices. 
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(pass_context=True) #deletes messages 
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    """Cleans out a textchat of trash."""
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@bot.command() # Repeats words.
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command() # puts a message if a user joins
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group() # makes a "Group" for the cool command. 
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot') # Adds a custom command for cool with the word "bot".
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@cool.command(name='ryan') # # Adds a custom command for cool with the word "ryan".
async def _ryan(ctx):
    """Is ryan cool?"""
    await ctx.send('Yes, Ryan | Roflush is cool')
    
@bot.command() # Adds github repo 
async def github(ctx):
    '''Github url redir'''
    await ctx.send('You can find the code at: https://github.com/Roflush/octobot')

@cool.command(name='ghost') # Adds a custom command for cool with the word "ghost".
async def _ghost(ctx):
    '''Is ghost cool?'''
    await ctx.send('Yes he drinks hennessy')

bot.run(token)