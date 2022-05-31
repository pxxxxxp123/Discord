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
        self.point = 0
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
        
