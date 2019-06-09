import discord
import random

client = discord.Client()

token = 'NTg3MDU2MDAxNjEwNTQ3Mzk3.XPxBKw.NNGNWA9l4hBMb6Qh1Rrb2_xFHPE'

@client.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(client.user.name)
    print(client.user.id)
    print('===============')
    activity = discord.Game(name="슈발뇽마음속")
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


        random.shuffle(man)
        await message.channel.send('-----------------------------------------')
        for i in range(0, ateam  ) :
            await message.channel.send(" - 발팀 -----> " + man[i] )
        await message.channel.send('-----------------------------------------')            
        for j in range(ateam , man_cnt) :
            await message.channel.send(" - 뇽팀 -----> " + man[j] )
        await message.channel.send('-----------------------------------------')            
        await message.channel.send("이봐 친구들 조합이 이상하면 적당히 섞어서하라규!")            
    else :
        await message.channel.send('슈발뇽이랑 친구할래?\n 사용법) 사다리 닉넴1 닉넴2 닉넴3 엔터 끝~')

client.run(token)
