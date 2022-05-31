import os
import csv
import asyncio
import random

def read_csv(csvfilename):
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows

class trivia:
    def __init__(self, lst, ctx):
        self.score = {}
        self.lst = lst
        self.answer = None
        self.ctx = ctx

    async def next_question(self):
        data_list = self.lst
        selection = random.choice(data_list)
        await self.ctx.send(selection[0])
        ans = selection[1:]
        shuffled = random.sample(ans, len(ans))
        await self.ctx.send('a. {} b. {} c. {}'.format(*shuffled))
        helper = {0:'a', 1:'b', 2: 'c'}
        self.answer = helper[shuffled.index(selection[1])]
        
    def add_player(self, user):
        #username = message.author.username
        self.score[user] = 0
        
    def add_point(self, user):
        self.score[user] += 1
        
    def get_score(self, message):
        await message.channel.send(f"{message.author.username} has {self.score[message.author.username]}")
    def get_leaderboard(self):
        helper = dict(sorted(self.score.items(), lambda x: x[1], reverse = True))
        pass
                                   
                    
        
