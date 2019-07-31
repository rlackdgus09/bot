import discord
import random
import datetime
import requests, json

client = discord.Client()

token = 'NTg3MDU2MDAxNjEwNTQ3Mzk3.XUGjcA.o7GhtgChJU8RVFtBelH8v27GOAM'

@client.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(client.user.name)
    print(client.user.id)
    print('===============')
    activity = discord.Game(name="슈발뇽 마음속♡")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith("사다리"):
        mans = message.content[4:]
        man = mans.split(" ")
        man_cnt = len(man)
        if man_cnt > 10:
            await message.channel.send('슈발뇽은 머리가 나뻐서 2팀까지 못짜네~ 미안행')            
            return None


        team = man_cnt / 2   
        sol = man_cnt % 2   
        
        ateam = int(team + sol)
        bteam = int(team)

        now = datetime.datetime.now()
        chetnum = int(now.second) % 4
        if chetnum == 0:
            await message.channel.send('슈발뇽이 최고에요~')                    
        if chetnum == 1:
            await message.channel.send('슈발뇽이랑 친구할래~')                    
        if chetnum == 2:
            await message.channel.send('슈발뇽한테 와라~')                    
        if chetnum == 3:
            await message.channel.send('슈발뇽이 될꺼야~')                                
        
        
        
        random.shuffle(man)
        await message.channel.send('-----------------------------------------')
        for i in range(0, ateam  ) :
            await message.channel.send(" - 슈팀 -----> " + man[i] )
        await message.channel.send('-----------------------------------------')            
        for j in range(ateam , man_cnt) :
            await message.channel.send(" - 발팀 -----> " + man[j] )
        await message.channel.send('-----------------------------------------')            
        await message.channel.send("우!유!빛!깔! 슈발뇽~♡♡")
        
        
   
        
client.run(token)
