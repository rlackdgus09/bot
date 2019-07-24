import discord
import random
import datetime
import requests, json

client = discord.Client()

token = 'NTg3MDk4NjM2MTAyNjY0MjA5.XTh1tA.s15bJ4_EIAaNu9D6FlWe29ZPsB8'

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
        
        
    if message.content.startswith("찾아죠"):
        pnick = message.content[4:]
        URL1 = 'https://api.neople.co.kr/cy/players?nickname='+pnick+'&wordType=full&apikey=70sfxPDKxA2crKkHvsElnbn0CYFtE6KK' 
        response1 = requests.get(URL1) 
        rcode1 = response1.status_code 
        if rcode1 != 200:
            await message.channel.send('정보가저오다 실패했썽~ 미안행♡♡')            
            return None
        await message.channel.send('정보를 찾고 있썽 기달려봥♡')                        
        pinfo = response1.json()
        rows = pinfo["rows"]
        row = rows[0]
        playerId = row["playerId"]
        nickname = row["nickname"]
        grade = row["grade"]
        await message.channel.send( str(grade) +'급 ' + nickname + '의 전적을 찾아보자~')
        print(playerId)

        URL2 = 'https://api.neople.co.kr/cy/players/' + playerId + '?apikey=70sfxPDKxA2crKkHvsElnbn0CYFtE6KK' 
        response2 = requests.get(URL2) 
        rcode2 = response2.status_code 
        if rcode2 != 200:
            await message.channel.send('정보가저오다 실패했썽~ 미안행♡♡')            
            return None
        idinfo = response2.json()
        clanName = idinfo["clanName"]
        ratingPoint = idinfo["ratingPoint"]
        maxRatingPoint = idinfo["maxRatingPoint"]
        tierName = idinfo["tierName"]
        records = idinfo["records"]

        await message.channel.send( clanName + ' 클랜에 몸담고 있네 요놈!')
        await message.channel.send( ' 현재 레이팅은 ' + str(ratingPoint) + ' 포인트! 최고 레이팅은 음 ' + str(maxRatingPoint) + ' 포인트!')
        await message.channel.send( ' ' + str(tierName) + ' 티어야!') 
        await message.channel.send( ' 전적은~ 음~') 

        records_cnt = len(records)
        for i in range(0, records_cnt  ) :
            record1 = records[i]
            gameTypeId = record1["gameTypeId"]
            gameTypeName = ' 공식'
            if gameTypeId == 'normal' :
                gameTypeName = ' 일반'
            winCount1 = record1["winCount"]
            loseCount1 = record1["loseCount"]
            stopCount1 = record1["stopCount"]
            await message.channel.send( gameTypeName + '은 ' + str(winCount1) + '승 ' + str(loseCount1) + '패 ' + str(stopCount1) + '중단') 

        await message.channel.send("우!유!빛!깔! 슈발뇽~♡♡")   
        
        

client.run(token)
