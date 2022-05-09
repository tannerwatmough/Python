import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99', help="Responds with a random quote from Brooklyn 99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "Title of your sex tape.",
        "Jake, why don't you do the right thing and jump out of a window?",
        "I asked them if they wanted to embarrass you, and they instantly said yes.",
        "Title of your sex tape.",
        "I ate one string bean. It tasted like fish vomit. That was it for me.",
        "Bingpot!",
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no dount no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice. !roll_dice <# of dice> <# of sides>')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='random', help='A random photo of Barclay, the best pup in the world!')
async def on_message(message):
    randomImage = random.choice(os.listdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot\\pictures"))
    os.chdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot\\pictures")
    await message.channel.send(file = discord.File(randomImage))
    os.chdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot")
    
@bot.command(name='hello', help='Barclay says hello!')
async def on_message(message):
    await message.channel.send("Woof! Hi! I'm Barclay!")

@bot.command(name='reflection', help='Barclay reacts to their reflection!')
async def on_message(message):
    randomImage = random.choice(os.listdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot\\reflections"))
    os.chdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot\\reflections")
    await message.channel.send(file = discord.File(randomImage))
    os.chdir("C:\\Users\\tanne\\Documents\\Discord Bot\\BarclayBot")
    await message.channel.send("Woof! Woof! Woof! Who is that?! Woof! Woof! Woof! *wiggles fluff butt*", tts = True)

bot.run(TOKEN)