import os
import csv
import asyncio
import random
import time

def read_csv(csvfilename):
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows

class trivia:
    def __init__(self, lst, ctx):
        self.score = {}
        self.lst = lst
        self.answer = None
        self.fullanswer = None
        self.ctx = ctx
        self.asked = []
        self.ongoing = True

    async def next_question(self):
        time.sleep(3)
        data_list = self.lst
        selection = random.choice(data_list)
        selection = list(filter(lambda x: x != '' ,selection))
        if selection not in self.asked:
            self.asked.append(selection)
            
            await self.ctx.send(selection[0])
            ans = selection[1:]
            shuffled = random.sample(ans, len(ans))
            print(shuffled)
            helper = {0:'a', 1:'b', 2: 'c', 3:'d'}
            self.answer = helper[shuffled.index(selection[1])]
            self.fullanswer = selection[1]
            print(self.answer)
            string = ''
            for i in range(len(shuffled)):
                string += '  ' + helper[i] + '. '+shuffled[i]
            await self.ctx.send(string)
            self.ongoing = True
        else:
            await self.next_question()

    async def correct_answer(self,message):
        await message.channel.send(f"Correct! {message.author.name} got it right")
        self.add_point(message)

    async def wrong_answer(self,message):
        await message.channel.send('Wrong!')
        await message.channel.send(f"The answer is {self.answer}, {self.fullanswer}")

    async def end_quiz(self, message):
        await message.channel.send(f"That is the last question")
        await message.channel.send(f"End of Quiz")
        await self.get_leaderboard(message.channel)

    def add_player(self, message):
        #username = message.author.username
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
        if len(helper) == 0:
            await ctx.send('No player found!')
        else:
            string = ''
            for key,value in helper:
                string += str(key) +': ' + str(value) + '\n'
            await ctx.send(string) 
                                   
                    
        
