import csv
data_list = []

with open("C:/Users/brenn/Desktop/Discord bot/userids.csv", mode="r") as pointer:
    csv_pointer = csv.reader(pointer)
    for row in csv_pointer:
        data_list.append(row)
    pointer.close()

#%%

import discord
from discord.ext import commands
import datetime
from random import*

token = 'OTc3ODM1NTYzMjY2NzY4OTU3.GjDkl-.Qej_sp1VNOkGcXa6BXPXlKCsGP80VDf9C9hmG0'
bannanid = 265758251705040896
bot = commands.Bot(command_prefix='!')

#prints statement when bot is online
@bot.event
async def on_ready():
    print('bot is online')
    txtgrp = bot.get_channel(528938798772387840)
    await txtgrp.send("bannanbot is online _ _gglets")
    

#responses to messages
aww_see_lst = ['Or C','or c', 'Aww See', 'aww see', 'aussie']
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if str(bannanid) in message.content:
        await message.channel.send('Shhh. Daddy might be working... He\'ll spank u Uwu')
    for i in aww_see_lst:
        if i in message.content:
            await message.channel.send('Badabida')
    await bot.process_commands(message)

        
#when people connect to vc
@bot.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    if channel.id != 373762193323458565 and member.id != bannanid: # Destiny of Chungus Voice Channel 1
        if before.channel is None and after.channel is not None:
            now = datetime.datetime.now()
            bannan = member.guild.get_member(bannanid)
            await bannan.send(f'{member} has joined voice channel in server: {member.guild.name} at {now.hour}:{now.minute}')

    else: #If chungus voice 1
        if before.channel is None and after.channel is not None:
            now = datetime.datetime.now()
            
@bot.command()
async def trivia(ctx):
    qns = random.choice(dlist)
    await ctx.send(qns)
    
@bot.command()
async def cf(ctx):
    cfoptions = ['heads','tails']
    response = random.choice(cfoptions)
    await ctx.send(response)


bot.run(token)
