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

    def add_player(self, message):
        #username = message.author.username
        print(message.author)
        self.score[message.author.name] = 0
        
    def add_point(self, message):
        self.score[message.author.name] += 1
        
    async def get_score(self, ctx):
        if ctx.author.name not in self.score:
            await ctx.send(f"{ctx.author.name} has not earned any point")
        else:
            await ctx.send(f"{ctx.author.name} has {self.score[ctx.author.name]}")

    async def get_leaderboard(self, ctx):
        helper = sorted(self.score.items(), key = lambda x: x[1], reverse = True)
        await ctx.send("=====Leaderboard=====")
        string = ''
        for key,value in helper:
            string += str(key) +': ' + str(value) + '\n'
        await ctx.send(string)
                                   
                    
        
