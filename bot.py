import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from coinflip import*
from PointSystem import*
import csv
import random
from trivia import*
import time

def read_csv(csvfilename):
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows

load_dotenv()
TOKEN = 'Input token'
bot = commands.Bot(command_prefix=';;')
trivia_lst = read_csv('random.csv')
game_trivia = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for server in bot.guilds:
        for channel in server.text_channels:
            if channel.permissions_for(server.me).send_messages:
                print(channel)
                #await channel.send('Bot is Up!')
                break
@bot.event
async def on_member_join(member):
    for server in bot.guilds:
        for channel in server.text_channels:
            if channel.permissions_for(server.me).send_messages:
                print(channel)
                await channel.send(f"Welcome {member.name} to Uniqlo!")
"""
class bot_join:
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    async def leave(ctx):
        await ctx.voice_client.disconnect()
"""
aww_see_lst = ['Or C','or c', 'Aww See', 'aww see', 'aussie', 'aw c', ]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    for i in aww_see_lst:
        if i in message.content.lower():
            await message.channel.send('BADABIDA')
    if message.content == 'raise-exception':
        raise discord.DiscordException6
    if game_trivia != None:
        if game_trivia.ongoing == True:
            message_lower = message.content.lower()
            if message_lower in ['a', 'b', 'c']:
                game_trivia.ongoing = False
                if message.author.name not in game_trivia.score.keys():
                    game_trivia.add_player(message)
                if message_lower == game_trivia.answer:
                    await game_trivia.correct_answer(message)
                else:
                    await game_trivia.wrong_answer(message)
                if len(game_trivia.asked) == len(trivia_lst):
                    game_trivia.ongoing = False
                    await game_trivia.end_quiz(message)
                    globals()['game_trivia'] = None
                else:
                    await message.channel.send('Next Question')
                    await game_trivia.next_question()
                
    await bot.process_commands(message)

@bot.command()
async def cf(ctx):
    await ctx.send(f"The Coin has landed on {flip()}")
    
###Trivia Bot Command###
@bot.command()
async def startT(ctx):
    if game_trivia == None:
        globals()['game_trivia'] = trivia(trivia_lst,ctx)
        await ctx.send('======Quiz has Started======')
        await game_trivia.next_question()
    else:
        await ctx.send(f"Game is already running!")

@bot.command()
async def stopT(ctx):
    await ctx.send(f"Quiz has stop")
    await game_trivia.get_leaderboard(ctx)
    globals()['game_trivia'] = None

@bot.command()
async def lb(ctx):
    if game_trivia != None:
        print(game_trivia.score)
        await game_trivia.get_leaderboard(ctx)

@bot.command()
async def score(ctx):
    if game_trivia != None:
        await game_trivia.get_score(ctx)

################
bot.run(TOKEN)
