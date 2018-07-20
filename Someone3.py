import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import time
import pymorphy2
import colorama
import inspect
import os
import sys

colorama.init()
client = discord.Client()
global ban
ban = []
global A
global i
global sl
global voi
global O
global mes
global mes2
global wait
global ostatus
global Mute
global extramute
global karmacheck
global pollmsg
global pollname
global sp
global embedp
embedp = None
sled = "0"
sp = []
pollname = ''
pollmsg = None
karmacheck = True
extramute = False
ostatus = None
wait = True
mes = 0
mes2 = [0,0,0,0,0]
O = []
voi = []
A = []
i = 0
sl = 0
Mute = []
morph = pymorphy2.MorphAnalyzer()

async def CallHerKarma(msg,typ):
    global karmacheck
    kmsg = ''
    if typ == 1:
        kmsg='Она добавила реакцию {0.emoji} на сообщение {0.message.author} \"{0.message.content}\" в канале {0.message.channel.mention}'.format(msg)
    elif typ == 2:
        kmsg='Она удалила реакцию {0.emoji} на сообщение {0.message.author} \"{0.message.content}\" в канале {0.message.channel.mention}'.format(msg)
    elif typ == 3:
        kmsg='Она зашла в воис {}'.format(msg)
    elif typ == 4:
        kmsg='Она изменила сообщение \"{0.content}\" в канале {0.channel.mention}'.format(msg)
    elif typ == 5:
        kmsg='Она написала сообщение \"{0.content}\" в канале {0.channel.mention}'.format(msg)
    sk = 'Внимание! Обнаружена <@{}>!\n{}'.format(sled,kmsg)
    ZID1 = '316260671778062338' #followers
    ZID2 = '324621511384367104' #zavod
    chank1 = client.get_channel(id = ZID1)
    chank2 = client.get_channel(id = ZID2)
    if karmacheck:
        karmacheck = False
        await client.send_message(chank1,sk)
        await client.send_message(chank2,sk)

async def delmes(msg):
    await asyncio.sleep(60)
    try:
        await client.delete_message(msg)
    except:
        pass
        
def bylen(lel):
    lel = lel[:lel.find(':')]
    lel = lel[:lel.find(':')]
    return len(lel)

def byName_key(person):
    return person.name

def len_penis(did):
    dk = 0
    dk2 = 99
    i9 = 0
    for i9 in range(len(did)):
        if i9 != 0:
            if dk2 > int(did[i9-1:i9+1]) and int(did[i9-1:i9+1]) > 9:
                dk2 = int(did[i9-1:i9+1])
        dk = dk + int(did[i9])
    dk = dk / len(did)
    #dk2 = dk2 / (len(did)-1)
    did = int(did)
    s9 = round((did % 100 + dk2) / dk, 1)
    return s9

def chelok(ms,ok):
    okok = ''
    if ms == 'человек':
        if ok % 10 > 1 and ok % 10 < 5 and ok % 100 != 11 and ok % 100 != 12 and ok % 100 != 13 and ok % 100 != 14:
            okok = 'a'
    elif ms == 'человек2':
        ms = 'человек'
        if ok % 10 == 1 and ok % 100 != 11 and ok % 100 != 12 and ok % 100 != 13 and ok % 100 != 14:
            okok = 'a'
    return '{} {}{}'.format(ok,ms,okok)
    #bu = morph.parse(ms)[0]
    #return '{} {}'.format(nm,bu.make_agree_with_number(nm).word)


async def statusserver(stat2):
    try:
        hyi = 0
        #await client.change_presence(game=discord.Game(name='статус сервера: {}'.format(stat2),type= 4))
    except:
        pass

async def background2():  
    global O
    global ostatus
    await client.wait_until_ready()
    await asyncio.sleep(12)
    l = len(O)
    sstat = 'на онлайн из {}'.format(chelok('человек2',len(O)))
    await client.change_presence(game=discord.Game(name= sstat,url = None, type = 3), status= ostatus)
    while True:
        if l != len(O):
            sstat = 'на онлайн из {}'.format(chelok('человек2',len(O)))
            await client.change_presence(game=discord.Game(name= sstat,url = None, type = 3), status= ostatus)
            l = len(O)
        await asyncio.sleep(5)
async def background():
    global ban
    global voi
    global mes
    global mes2
    global wait
    global O
    await client.wait_until_ready()
    await asyncio.sleep(10)
    while True:
        if wait:
            print('Инициализация (BG)')
        else:
            
            mes2.append(mes)
            mes2.remove(mes2[0])
            mes = 0
            await upban(0)
            voi2 = []
            bt3 = len(O)-1
            while bt3 > -1:
                if voi.count(O[bt3][0].id) != 0:
                    O[bt3][1] = 2
                O[bt3][1] = O[bt3][1] - 0.15
                if O[bt3][1] < 0 :
                    O.remove(O[bt3])
                bt3 -=1
            for i8 in range(len(ban)):
                if voi.count(ban[i8][0]) != 0:
                    ban[i8][1] = ban[i8][1] + 4
                    voi2.append(ban[i8][0])
                x = ban[i8][1]
                ban[i8][1] = (x-((0.000000000000000000000000000000001 * (x ** 10))+0.1))
                #print(x,ban[i8][1])
               # ban[i8][1] = (x-((0.000001 * (x ** 2))+0.2))
              #  ban[i8][1] = (ban[i8][1] - ((1.012 ** (0.09 * x )) - 0.8 ))    
                if ban[i8][1] < 0:
                    ban[i8][1] = 0
            i12 = 0
            for i12 in range(len(voi)):
                if voi2.count(voi[i12]) == 0 :
                    ban.append([voi[i12],3.87])
                    print(voi[i12],3.87)
            voi = voi2
            voi2 = []
            await upban(1)
            await asyncio.sleep(60)


async def upban(q2:int):
    global ban      
    if q2 == 0:
        b = open('Active.txt', 'r',encoding='utf-8')
        ban = []
        bk = 0
        for bk, bline in enumerate(b):
            if bk == 0:
                pass
            else:
                bline = bline.replace("\n", "")
                #print(bline)
                ban.append([])
                ban[bk-1].append(bline[:bline.find('~')])
                try:
                    ban[bk-1].append(float(bline[bline.find('~')+1:len(bline)]))
                except:
                    pass
            bk += 1
        b.close()
    elif q2 == 1:
        bn = open('Active.txt', 'w',encoding='utf-8')
        i1 = 0
        bn.write('_________________________\n')
        for i1 in range(len(ban)):
            bn.write(str(ban[i1][0])+'~'+str(ban[i1][1])+'\n')
        bn.close()





@client.event
async def on_ready():
    global A
    global O
    global wait
    global ostatus
    print ("Someone v 1.9 активирована")
    print ("Имя: {}".format(client.user.name))
    print ("ID: {}".format(client.user.id))
    print ("____________________________")
    ZID = '316260671778062338' #followers
    chan2 = client.get_channel(id = ZID)
    await upban(0)
    for member in chan2.server.members:
        A.append(member)
        after = member
        if str(member.status) == 'offline':
            ostatus = member.status
            await client.change_presence(status=ostatus)
        if after.server.id == '313762360768856075' and str(after.voice_channel) != 'Канал АФК' and after.self_deaf == False and after.voice_channel != None:
            voi.append(after.id)           
            O.append([after,2])
    A = sorted(A, key = byName_key)
    print(str(voi))
    wait = False

@client.event
async def on_reaction_add(reaction1, user1):
    global O
    global pollmsg
    global pollname
    global sp
    global embedp
    try:
        if reaction1.message.id == pollmsg.id:
            #emojipoll = ['u\0030\u20e3','u\0031\u20e3','u\0033\u20e3','u\0034\u20e3','u\0035\u20e3','u\0036\u20e3','u\0037\u20e3','u\0038\u20e3','u\0039\u20e3','🔟']
            emojipoll = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
            #emojipoll = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:' ]
            #print(str(reaction1.emoji))
            kp = emojipoll.index(str(reaction1.emoji))
            #print(kp)
            if kp > -1:
                sp[kp][1] = sp[kp][1] +1
                #print(sp) 
                embedp=discord.Embed(title="Опрос!", description=pollname, color=0x8238cb)
                ip = 0
                ipmax = 1
                ipall = 0
                for ip in range(len(sp)):
                    ipall = ipall + sp[ip][1]
                    if sp[ip][1] > ipmax:
                        ipmax = sp[ip][1]
                if ipall == 0:
                    ipall = 1
                #print(ipmax)
                #print(ipall)
                ip = 0
                for ip in range(len(sp)):
                    embedp.add_field(name='{}) {} - {}%'.format(ip+1,sp[ip][0],round(sp[ip][1]/ipall*100,1)), value='█'+'█' * round(37 * sp[ip][1]/ipmax), inline=False)
                await client.edit_message(pollmsg,embed=embedp)
    except:
        pass
    if str(reaction1.message.author.id) == sled:
        await CallHerKarma(reaction1,1)
    if reaction1.message.server.id == '313762360768856075' and reaction1.message.author.bot == False:
        bt2 = 0
        btf2 = True
        for bt2 in range(len(O)):
            if O[bt2][0] == reaction1.message.author:
                O[bt2][1] = 1
                btf2 = False
        if btf2:
            O.append([reaction1.message.author,0.5])


@client.event
async def on_reaction_remove(reaction2, user2):
    global O
    global pollmsg
    global pollname
    global sp
    global embedp
    try:
        if reaction2.message.id == pollmsg.id:
            #emojipoll = ['u\0030\u20e3','u\0031\u20e3','u\0033\u20e3','u\0034\u20e3','u\0035\u20e3','u\0036\u20e3','u\0037\u20e3','u\0038\u20e3','u\0039\u20e3','🔟']
            emojipoll = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
            #emojipoll = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:' ]
            #print(str(reaction2.emoji))
            kp = emojipoll.index(str(reaction2.emoji))
            #print(kp)
            if kp > -1:
                sp[kp][1] = sp[kp][1] -1
                if sp[kp][1] < 0:
                    sp[kp][1] = 0
                #print(sp) 
                embedp=discord.Embed(title="Опрос!", description=pollname, color=0x8238cb)
                ip = 0
                ipmax = 1
                ipall = 0
                for ip in range(len(sp)):
                    ipall = ipall + sp[ip][1]
                    if sp[ip][1] > ipmax:
                        ipmax = sp[ip][1]
                if ipall == 0:
                    ipall = 1
                #print(ipmax)
                #print(ipall)
                ip = 0
                for ip in range(len(sp)):
                    embedp.add_field(name='{}) {} - {}%'.format(ip+1,sp[ip][0],round(sp[ip][1]/ipall*100,1)), value='█'+'█' * round(37 * sp[ip][1]/ipmax), inline=False)
                await client.edit_message(pollmsg,embed=embedp)
    except:
        pass
    if str(reaction2.message.author.id) == sled:
        await CallHerKarma(reaction2,2)
    if reaction2.message.server.id == '313762360768856075' and reaction2.message.author.bot == False:
        bt2 = 0
        btf2 = True
        for bt2 in range(len(O)):
            if O[bt2][0] == reaction2.message.author:
                O[bt2][1] = 1
                btf2 = False
        if btf2:
            O.append([reaction2.message.author,0.5])


@client.event
async def on_voice_state_update(before, after):
    
    global voi
    global O
    global wait
    if wait:
        print('Инициализация (VS)')
    else:
        if after.id == sled:
            await CallHerKarma(after.voice_channel,3)
        if after.server.id == '313762360768856075' and after.voice_channel == None:
            try:
                print('Из {} вышел {}'.format(before.voice_channel,str(after)))
            except:
                print('Из {} вышел {}'.format(before.voice_channel,after.id))
        elif after.server.id == '313762360768856075' and after.voice_channel != before.voice_channel:
            try:
                print('В {} зашел {}'.format(after.voice_channel,str(after)))
            except:
                print('В {} зашел {}'.format(after.voice_channel,after.id))
        #if after.server.id == '313762360768856075':
        #    print(after.voice.deaf,after.voice.mute,after.voice.self_mute,after.voice.self_deaf,after.voice.is_afk,after.voice.voice_channel)
        if after.server.id == '313762360768856075' and str(after.voice_channel) != 'Канал АФК' and after.self_deaf == False and after.voice_channel != None:
        #if after.is_afk == False:
            if voi.count(after.id) == 0:
                voi.append(after.id)
            i14B = True
            for i14 in range(len(O)):
                if O[i14][0] == after:
                    i14B = False
                    break
            if i14B:
                O.append([after,0])
        if after.voice_channel == None or str(after.voice_channel) == 'Канал АФК' or after.self_deaf == True:
            try:
                voi.remove(after.id)
            except:
                pass
@client.event
async def on_message_delete(messaged):
    global O
    
    if messaged.server.id == '313762360768856075' and messaged.author.bot == False:
        bt2 = 0
        btf2 = True
        for bt2 in range(len(O)):
            if O[bt2][0] == messaged.author:
                O[bt2][1] = 1
                btf2 = False
        if btf2:
            O.append([messaged.author,0.5])

@client.event
async def on_message_edit(mbefore, mafter):
    global O
    if str(mafter.author.id) == sled:
        await CallHerKarma(mbefore,4)
    if mafter.server.id == '313762360768856075' and mafter.author.bot == False:
        bt2 = 0
        btf2 = True
        for bt2 in range(len(O)):
            if O[bt2][0] == mafter.author:
                O[bt2][1] = 1
                btf2 = False
        if btf2:
            O.append([mafter.author,0.5])

@client.event
async def on_message(message):
    global A
    global O
    global i
    global sl
    global ban
    global mes
    global mes2
    global voi
    global wait
    global ostatus
    global Mute
    global extramute
    global karmacheck
    global pollmsg
    global pollname
    global sp
    global embedp
    ping = message.mentions
    if ping.count(client.user):
        try:
            print("\x1b[34;43m"+str(message.author)+': '+message.content+"\x1b[0m")
        except:
            try:
                print("\x1b[34;43m"+message.author.id+': '+message.content+"\x1b[0m")
            except:
                print("\x1b[34;43m"+message.author.id+"\x1b[0m")
    if wait:
        print('Инициализация (MSG)')
        if message.content == "Zbotwait":
            wait = False
        elif message.content.startswith('Zbot'):
            await asyncio.sleep(2)
            msg = await client.send_message(message.channel,'```Идет инициализация, пожалуйста, повторите попытку через несколько секунд...```')
            await delmes(msg)
    else:
        if message.author.id == sled:
            await CallHerKarma(message,5)
        if message.content.startswith('Zbot') or message.content.startswith('Bot2mute'):
            sid = ''
            spl = message.content.split()
            for ispl in range(len(spl)):
                if len(spl[ispl]) == 18 and spl[ispl].isdigit():
                    sid = spl[ispl]
            if sid == '':
                sid = message.content[message.content.find('<'):message.content.find('>')]
                sid = sid.replace('<','')
                sid = sid.replace('>','')
                sid = sid.replace('@','')
                sid = sid.replace('!','')
            us = message.channel.server.get_member(sid)
            if us == None:
                us = message.author

        try:
            if message.server.id == '313762360768856075' and message.author.bot == False:
                if message.channel.id !='324621511384367104':
                    mes +=1
                    await upban(0)
                    bt = 0
                    btf = True
                    for bt in range(len(ban)):
                        if ban[bt][0] == message.author.id:
                            if message.attachments != []:
                                ban[bt][1] = ban[bt][1] + 2
                            else:
                                ban[bt][1] = ban[bt][1] + 1
                            await upban(1)
                            btf = False
                    if btf:
                        ban.append([message.author.id,1])
                        await upban(1)

                bt2 = 0
                btf2 = True
                for bt2 in range(len(O)):
                    if O[bt2][0] == message.author:
                        O[bt2][1] = 1
                        btf2 = False
                if btf2:
                    O.append([message.author,1])
        except:
            pass

        if (Mute.count(message.author) > 0 or extramute) and (message.author != client.user) and (message.server.id == '313762360768856075') :
            try:
                await client.delete_message(message)
            except:
                print('Ошибка удаления')
                
        elif message.content == 'Zbotinviz':
            if message.author.id == client.user.id:
                sa = None
                for member3 in message.channel.server.members:
                    if str(member3.status) == 'offline':
                        ostatus = member3.status
                        break
                if str(message.author.status) != 'offline':
                    await client.change_presence(status=ostatus)
                    print('Now you offline')
                else:
                    ostatus = None
                    await client.change_presence(status=ostatus)
                    print('Now you online')
                await client.delete_message(message)
                     
        elif message.content == "Zbotmute all":
            if extramute:
                extramute = False
            else:
                extramute = True
        elif message.content.startswith("Zbotpoll"):
            if message.author.id == client.user.id:
                if  message.content == 'Zbotpoll up':
                    try:
                        await client.delete_message(pollmsg)
                    except:
                        pass
                    pollmsg = await client.send_message(message.channel,embed=embedp)
                    emojipoll = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
                    ip = 0
                    for ip in range(len(sp)):
                        sp[ip][1] = sp[ip][1] -1
                        await client.add_reaction(pollmsg,emojipoll[ip])
                else:
                    sp = message.content.split('_')
                    pollname = sp[1]
                    embedp=discord.Embed(title="Опрос!", description=pollname, color=0x8238cb)
                    hyi = sp.pop(0)
                    hyi = sp.pop(0)
                    ip = 0
                    for ip in range(len(sp)):
                        embedp.add_field(name='{}) {} - 0%'.format(ip+1,sp[ip]), value='█', inline=False)
                        sp[ip] = [sp[ip],-1]
                    pollmsg = await client.send_message(message.channel,embed=embedp)
                    emojipoll = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
                    ip = 0
                    for ip in range(len(sp)):
                        await client.add_reaction(pollmsg,emojipoll[ip])




        elif message.content.startswith("Zbotmute"):
            if message.author.id == client.user.id:
                if us == None:
                    await client.send_message(message.channel,'```Вы не можете замутить себя```')
                else:
                    await client.send_message(message.channel,'```{} замутил {}```'.format(message.author,str(us)))
                    Mute.append(us)
        elif message.content.startswith("Zbotunmute"):
            if message.author.id == client.user.id:
                try:
                    Mute.remove(us)
                    await client.send_message(message.channel,'```{} размутил {}```'.format(message.author,str(us)))
                except:
                    pass
        elif message.content.startswith("Zbotwarn"):
            if message.author.id == client.user.id:
                s = message.content.split()
                M6 = message.mentions
                sadd = ''
                warn = '!'
                s.append('')
                for j4 in range(len(M6)):
                    sadd = sadd + M6[j4].mention + ' '
                if s[1] == 'anime':
                    warn = 'Все, что связано с аниме, должно находиться в канале #anime, проследуйте туда или в противном случае получите мут по 1.6'
                elif s[1] == 'dota':
                    warn = 'Для обсуждения Доты есть специальный канал #dota, пожалуйста, пройдите туда. Чтобы попасть в него, вам надо иметь роль Dota (в #find-party надо прописать Bot2rank Dota2), проследуйте туда или в противном случае получите мут'
                elif s[1].find('!') != -1:
                    morph = pymorphy2.MorphAnalyzer()
                    mms = message.content
                    mms = mms.replace('Zbotwarn !','')
                    mk = (mms.find('@'))-1
                    if mk == -2:
                        mk = len(mms)
                    ms = mms[:mk]
                    ms = ms.strip()
                    ms3 = ms.split()
                    mss = ''
                    mss2 = ''
                    if ms == '':
                        warn = '!'
                    else:
                        for mi in range(len(ms3)):
                            ms2 = morph.parse(ms3[mi])[0]
                            mch = ms2.inflect({'gent'})
                            if mch == None:
                                mss = mss + ms3[mi] + ' '
                            else:
                                mss = mss + mch.word + ' '
                            mss2 = ms.replace(' ','-')
                        warn = 'Для обсуждения {}есть специальный канал #{}, пожалуйста, пройдите туда. Чтобы попасть в него, вам надо иметь роль \'{}\''.format(mss,mss2,ms)
                else:
                    mms = message.content
                    mms = mms.replace('Zbotwarn','')
                    mk = (mms.find('@'))-1
                    if mk == -2:
                        mk = len(mms)
                    ms = mms[:mk]
                    ms = ms.strip()
                    warn = ms
                await client.delete_message(message)
                await client.send_message(message.channel,'{}\nПредупреждение!\n```{}```'.format(sadd,warn))

        elif message.content.startswith("Zbotpurge"):
            if message.author.id == client.user.id:
                channel = message.channel
                s = message.content.split()
                s.append('')
                s.append('')
                try:
                    search_range = int(s[1])
                except:
                    search_range = 50
                ch = True      

                if s[2] == 'all':
                    ch = False   
                deleted = 0 
                async for msg in client.logs_from(channel, limit=search_range, before=message):
                    try:
                        if ch:
                            if msg.author == us:
                                await client.delete_message(msg)
                                await asyncio.sleep(0.21)
                                deleted += 1
                        else:
                            await client.delete_message(msg)
                            await asyncio.sleep(0.21)
                            deleted += 1
                    except:
                        print('Ошибка удаления')
            
                await client.send_message(channel,'```Очищено сообщений: {}```'.format(deleted))

        elif message.content.startswith("Zbotsomeone"):
           # if message.author.id == client.user.id:
            if message.channel.id == '324621511384367104':
                i +=1
                print(i)
                sl +=1
                #while True:
                N = random.randint(0,(message.channel.server.member_count))
                    #if str(A[N].status) != 'offline':
                    #    break
                await asyncio.sleep(sl)
                sl -=1
                await client.send_message(message.channel,'{} сказал: \"{}, {}\"'.format(str(message.author),str(A[N]),message.content[message.content.find(' ')+1:len(message.content)]))
    
        elif message.content == "Zbotinit":
            if message.author.id == client.user.id:
                wait = True
                voi = []
                O = []
                ban = []
                A = []
                await upban(0)
                for member in message.channel.server.members:
                    A.append(member)
                    after = member
                    if after.server.id == '313762360768856075' and str(after.voice_channel) != 'Канал АФК' and after.self_deaf == False and after.voice_channel != None:
                        voi.append(after.id)
                        O.append([after,2])
                A = sorted(A, key = byName_key)
                wait = False
                await client.send_message(message.channel,'```Инициализация завершена```')
                await asyncio.sleep(5)
                karmacheck = True

        elif message.content.startswith('Bot2mute'):
            M = ['','']
            msgs = message.content.split()
            M[0] = msgs[2]
            for i19 in range(len(msgs)-3):              
                M[1] =  M[1] + msgs[i19+3] + ' '
            if M[1] == '':
                M[1] = 'причина не указана'
            if M[0].find('h') != -1:
                sm = M[0]
                M[0] = sm[:sm.find('h')] + ' ч.'
            elif M[0].find('d') != -1:
                sm = M[0]
                M[0] = sm[:sm.find('d')] + ' д.'
            elif M[0].find('w') != -1:
                sm = M[0]
                M[0] = sm[:sm.find('w')] + ' нед.'
            elif M[0].find('m') != -1:
                sm = M[0]
                M[0] = sm[:sm.find('m')] + ' мес.'
            elif M[0].find('y') != -1:
                sm = M[0]
                M[0] = sm[:sm.find('y')] + ' г.'
            else:
                sm = M[0]
                M[0] = sm + ' мин.'


            try:
                if us == client.user:
                    await client.send_message(message.channel,'```{} замутил {} на {} по причине: {}```'.format(message.author,message.author,M[0],M[1]))
                else:
                    await client.send_message(message.channel,'```{} замутил {} на {} по причине: {}```'.format(message.author,str(us),M[0],M[1]))
            except:
                print('```{} замутил {} на {} по причине: {}```'.format(message.author.id,us.id,M[0],M[1]))


        elif message.content.startswith('Zbotrole'):
            s6 = ''
            s7 = ''
            s7b = False
            C = message.server.role_hierarchy
            C = sorted(C, key = byName_key)
            for i6 in range(len(C)):
                s6 = s6 +'{}, '.format(C[i6].name)
                if len(s6) > 1900:
                    s7 = s6+'и др.'
                    s7b = True
            s6 = s6[:len(s6)-2]
            if message.content =='Zbotroles':
                if s7b:
                    pass
                else:
                    s7 = s6
                msg = await client.send_message(message.channel,'```{}```'.format(s7))
                await delmes(msg)

            elif message.content.startswith('Zbotroleinfo'):
                col2 = 0xffffff
                s3 = ['']
                rid = message.content
                rid = rid.replace('Zbotroleinfo ','')
                if s6.find(rid) != -1:
                    rols3 = ''
                    ridi = 0
                    B = sorted(message.channel.server.members, key = byName_key)
                    for member4 in B:
                        rols3 = ''
                        rol3 = member4.roles
                        rol3.sort()
                        for i55 in range(len(rol3)):
                            if rol3[i55].name == rid:
                                col2 = rol3[i55].colour
                                s3[ridi] = s3[ridi]+'{}, '.format(str(member4))
                                break
                        if len(s3[ridi]) > 1000:        
                            s3[ridi] = s3[ridi][:len(s3[ridi])-2]
                            ridi +=1
                            s3.append('')
                    s3[ridi] = s3[ridi][:len(s3[ridi])-2]
                    ij = 0
                    embed3=discord.Embed(title="Обладатели роли {}, страница {} из {}:".format(rid,ij+1,ridi+1),description='```{}```'.format(s3[ij]),color=col2)
                    msg = await client.send_message(message.channel,embed=embed3)
                    await client.add_reaction(msg,'🔽')
                    await client.add_reaction(msg,'🔼')
                    while True:
                        try:
                            embed3=discord.Embed(title="Обладатели роли {}, страница {} из {}:".format(rid,ij+1,ridi+1),description='```{}```'.format(s3[ij]),color=col2)
                            await client.edit_message(msg,embed=embed3)              
                            res = await client.wait_for_reaction(['🔽', '🔼'],timeout=60, message=msg)
                            if res == None :
                                await delmes(msg)
                                break
                            elif res.reaction.emoji == '🔽':
                                ij +=1
                                if ij > ridi:
                                    ij -=1 
                            elif res.reaction.emoji == '🔼':
                                ij -=1
                                if ij < 0:
                                    ij +=1 
                        except:
                            break 
                else:
                    msg = await client.send_message(message.channel,'```Роль не найдена. Введите Zbotroles, чтобы увидеть весь список ролей на серере.```')
                await delmes(msg)

        elif message.content.startswith('Zbotboobs'):            
            us3 = us
            bob = us.id
            bob2 = 0
            bobk = 0
            bo = 0
            while True:
                bob2 = (int(bob[int(bob[bo])]) + int(bob[len(bob)-1]) + int(bob[len(bob)-bo-1])) / (len(bob)-int(bob[int(bob[bo])]))
                if bob2 > 5.2:
                    bo += 1
                else:
                    break
                if bo > len(bob)-2:
                    bob2 = 0
                    break
            sdd2 = 'Ваш размер груди: {}'.format(round(bob2,1))
            embedd2=discord.Embed(description=sdd2,color=0xff00ff)
            embedd2.set_author(name=us3.name, icon_url=us3.avatar_url)
            embedd2.set_footer(text='ID: {}'.format(us3.id))
            msg = await client.send_message(message.channel,embed=embedd2)
            await delmes(msg)
            
        elif message.content.startswith('Zbotdick'):
            us2 = us
            pepa2 = 0
            minpepa = 99
            minpepas = ''
            minpepak = 0
            maxpepak = 0
            maxpepa = 0
            maxpepas = ''
            i11 = 0
            cold = 0xc0c0c0
            for member5 in message.channel.server.members:
                if len_penis(member5.id) >= maxpepa:
                    if len_penis(member5.id) == maxpepa:
                        maxpepak +=1
                        if maxpepak > 3:
                            maxpepas = str(maxpepak) + ' чел.'
                        else:
                            maxpepas = maxpepas + ', ' +str(member5)
                    else: 
                        maxpepak = 1
                        maxpepas = str(member5)
                        maxpepa = len_penis(member5.id)               

                elif len_penis(member5.id) <= minpepa:
                    if len_penis(member5.id) == minpepa:
                        minpepak +=1
                        if minpepak > 3:
                            minpepas = str(minpepak) + ' чел.'
                        else:
                            minpepas = minpepas + ', ' +str(member5)
                    else:
                        minpepak = 1
                        minpepas = str(member5)
                        minpepa = len_penis(member5.id)
                            
                pepa2 = pepa2 + len_penis(member5.id)
            pepa2 = round(pepa2 / message.channel.server.member_count , 1 )
            if len_penis(us2.id) > pepa2 +4:
                cold = 0x00ff00
            if len_penis(us2.id) < pepa2 +4 and len_penis(us2.id) > pepa2 -4:
                cold = 0xffff00
            if len_penis(us2.id) < pepa2 -4:
                cold = 0xff0000
            sdd2 = '\nСредний размер члена на сервере: {} см\nСамый большой член: {} см у {}\nСамый маленький член: {} см у {}'.format(pepa2,maxpepa,maxpepas,minpepa,minpepas)

            baz = str(len_penis(us2.id)) + ' см'
            if us2.id == '329341636574183424' :
                baz = 'базука'
            sdd = 'Ваш член: {}{}'.format(baz,sdd2)
            embedd=discord.Embed(description=sdd,color=cold)
            embedd.set_author(name=us2.name, icon_url=us2.avatar_url)
            embedd.set_footer(text='ID: {}'.format(us2.id))
            try:
                msg = await client.send_message(message.channel,embed=embedd)
            except:
                msg = await client.send_message(message.channel,'```{}\n\n{}```'.format(us2.name,sdd))
            await delmes(msg)



        
        elif message.content.startswith('Zbotstatus'):
            statdict = {'online': 'в сети:small_blue_diamond:' , 'offline' : 'не в сети:black_medium_small_square:' , 'idle' : 'не активен:small_orange_diamond:' , 'dnd' : 'не беспокоить:small_red_triangle_down:' , 'invisible' : 'невидимый:white_medium_small_square:'}
            msg = message.content
            if msg.find('online') != -1:
                if message.server.id == '313762360768856075':
                    son = ''
                    for i15 in range(len(O)):
                        son = son + str(O[i15][0]) + ', '
                        if len(son) > 1900:
                            son = son + ' и др...'
                            break
                    son = son[:len(son)-2] 
                    msg = await client.send_message(message.channel,'```Активный онлайн: {}\n{}```'.format(len(O),son))
                    await delmes(msg)
            elif msg.find('active') != -1:
                if message.server.id == '313762360768856075':
                    await upban(0)
                    akt = 0
                    sakt = ''
                    i7 = 0 
                    aktsrs = 0
                    aktsr2s = 0
                    aktkoefs = 0
                    ban2 = []
                    for i7 in range(len(ban)):                  
                        if ban[i7][1] > 0:
                            aktsrs = aktsrs+1
                            aktsr2s = aktsr2s + ban[i7][1]
                        ban2.append([ban[i7][1],ban[i7][0]])
                    i7 = 0 
                    ban2.sort(reverse=True)
                    for i7 in range(len(ban2)):
                        aktkoefs = ban2[i7][0]
                        if aktkoefs == 0:
                            break
                        if round(aktkoefs / (aktsr2s/aktsrs), 2 ) >= 1:
                            akt += 1
                            for member6 in message.channel.server.members:
                                if str(member6.id) == ban2[i7][1]:
                                    sakt = sakt + str(member6) + ', '
                                    if len(sakt) > 1900:
                                        sakt = sakt + ' и др...'
                                        break
                    sakt = sakt[:len(sakt)-2]                
                    msg = await client.send_message(message.channel,'```Активных людей: {}\n\n{}```'.format(akt,sakt))
                    await delmes(msg)

            elif msg.find('server') != -1:
                ss = message.server
                k = 0
                j = 0
                rol4 = []
                admo = 0
                muto = 0
                pepa = 0
                vois = 0
                A = []
                for member in message.channel.server.members:
                    pepa = pepa + len_penis(member.id)
                    if member.voice_channel != None:
                        vois +=1
                    if str(member.status) != 'offline':
                        k +=1
                    rol4 = member.roles
                    rol4.reverse()
                    for i24 in range(len(rol4)):
                        if (rol4[i24].name.find('Access') != -1) and (str(member.status) != 'offline'):
                            admo += 1
                        if (rol4[i24].name.find('Muted') != -1):
                            muto += 1
                d3= ss.created_at
                ltime3 = '{}.{}.{}'.format(d3.day,d3.month,d3.year)
                if message.server.id == '313762360768856075':
                    await upban(0)
                    akt = 0
                    i7 = 0 
                    aktsrs = 0
                    aktsr2s = 0
                    aktkoefs = 0
                    for i7 in range(len(ban)):                  
                        if ban[i7][1] > 0:
                            aktsrs = aktsrs+1
                            aktsr2s = aktsr2s + ban[i7][1]
                    i7 = 0        
                    for i7 in range(len(ban)):          
                        aktkoefs = ban[i7][1]
                        if round(aktkoefs / (aktsr2s/aktsrs), 2 ) >= 1:
                            akt += 1
                    

                    
                    mes4 = 0
                    for i17 in range(len(mes2)):
                        mes4 = mes4 + mes2[i17]
                    mes4 = mes4 // len(mes2)
                    sd = 'Активный онлайн: {}\nПостоянный актив: {}\nВ муте: {}\nАдминов онлайн: {}\nВ среднем сообщений за минуту: {}\n'.format(chelok('человек',len(O)),chelok('человек',akt),chelok('человек',muto),admo,mes4)
                else:
                    sd = ''
                pepa = round(pepa / message.channel.server.member_count , 1 )
                s4 = 'На сервере: {}\nОнлайн: {}\nВ воисе: {}\n{}Средний размер члена на сервере: {} см\nДата создания: {}\nСоздатель: {}\nРегион: {}\nСервер большой: {}'.format(chelok('человек',message.channel.server.member_count),chelok('человек',k),chelok('человек',vois),sd,pepa,ltime3,ss.owner,ss.region,ss.large)
                    
                if message.server.id == '313762360768856075':
                    mes3 = 0
                    for i16 in range(len(mes2)):
                        mes3 = mes3 + mes2[i16]
                    mes3 = mes3 // len(mes2)
                    stat = len(O)*25 + akt * mes3 + admo * 200 + len(voi) * 80 + muto * 5
                    if stat < 1300:
                        stats = 'мертв'
                        colstat = 0x000000
                        tumb = 'https://cdn.discordapp.com/emojis/392151029342273547.png'
                    elif stat >= 1300 and stat < 2000:
                        stats = 'некая активность'
                        tumb = 'https://cdn.discordapp.com/emojis/357948185810829312.png'
                        colstat = 0x858585
                    elif stat >= 2000 and stat < 3000:
                        tumb = 'http://www.emoji.co.uk/files/twitter-emojis/symbols-twitter/11172-wheelchair-symbol.png'
                        stats = 'начало возрождения'
                        colstat = 0xffff80
                    elif stat >= 3000 and stat < 3500:
                        stats = 'почти живой'
                        tumb = 'https://cdn.discordapp.com/emojis/414242070446866432.png'
                        colstat = 0x0080ff
                    elif stat >= 3500 and stat < 5000:
                        stats = 'живой'
                        colstat = 0x00ff00
                        tumb = ss.icon_url
                    elif stat >= 5000 :
                        stats = 'сильная активность'
                        tumb = 'https://cdn.discordapp.com/emojis/414242084107714570.png'
                        colstat = 0xff0000
                    embed4=discord.Embed(description=s4,color = colstat)
                    embed4.set_footer(text='Статус сервера: {}'.format(stats))
                    await statusserver(stats)
                    embed4.set_thumbnail(url=tumb)
                    print('Поинты активности: {}'.format(stat))
                else:
                    embed4=discord.Embed(description=s4)
                    embed4.set_thumbnail(url=ss.icon_url)
                embed4.set_author(name=ss.name, icon_url=ss.icon_url)
                try:               
                    msg = await client.send_message(message.channel,embed=embed4)
                except:
                    msg = await client.send_message(message.channel,'```{}\n\n{}```'.format(ss.name,s4))
                await delmes(msg)
            elif msg.find('admins') != -1:
                s2 = []
                rols2 = ''
                for member2 in message.channel.server.members:
                    rols2 = ''
                    rol2 = member2.roles
                    for i22 in range(len(rol2)):
                        if rol2[i22].name.find('Access') != -1:
                            ctrlstatus = str(member2.status)
                            OO = 0
                            for OO in range(len(O)):
                                if O[OO][0] == member2 and ctrlstatus == 'offline':
                                    ctrlstatus = 'invisible'
                                    break
                            s2.append('{}: {}'.format(member2.name,statdict[str(ctrlstatus)]))
                            break
                s2s = sorted(s2, key = bylen)
                s2x = ''
                for iss in range(len(s2s)):
                    s2x = s2x + s2s[iss]+'\n'
                embed2=discord.Embed(title="Онлайн статус админов:",description=s2x,color=0xff0000)
                msg = await client.send_message(message.channel,embed=embed2)
                await delmes(msg)
            elif msg.find(' bots') != -1:
                s2 = []
                for member2 in message.channel.server.members:
                    if member2.bot:
                        ctrlstatus = str(member2.status)
                        s2.append('{}: {}'.format(member2.name,statdict[str(ctrlstatus)]))
                s2s = sorted(s2, key = bylen)
                s2x = ''
                for iss in range(len(s2s)):
                    s2x = s2x + s2s[iss]+'\n'
                embed2=discord.Embed(title="Онлайн статус ботов:",description=s2x,color=0x00ffad)
                msg = await client.send_message(message.channel,embed=embed2)
                await delmes(msg)
            else:
                d = us.joined_at
                d2= us.created_at
                ltime = '{}.{}.{}'.format(d.day,d.month,d.year)
                ltime2 = '{}.{}.{}'.format(d2.day,d2.month,d2.year)
                rol = []
                toprol = ''
                rol = us.roles
                toprol = us.top_role
                if str(rol[0].name).find('everyone') == -1:
                    toprol = rol[0].name
                    rol.reverse()
                try:
                    toprol = toprol.replace('@everyone','everyone')
                except:
                    toprol.name = toprol.name.replace('@everyone','everyone')
                rol[0].name = rol[0].name.replace('@everyone','everyone')
                rols = ''
                col = 0xc0c0c0
                for i2 in range(len(rol)):
                    if rol[i2].hoist:
                        col = rol[i2].colour
                    rols = rols+'{}, '.format(rol[i2].name)
                rols = rols[:len(rols)-2]
                aktsr = 0
                aktsr2 = 0
                aktkoef = 0
                await upban(0)
                for i13 in range(len(ban)):
                    if ban[i13][1] > 0:
                        aktsr = aktsr+1
                        aktsr2 = aktsr2 + ban[i13][1]
                    if ban[i13][0] == us.id:
                        aktkoef = ban[i13][1]
                aktkoef = round(aktkoef / (aktsr2/aktsr), 2 )
                baz = str(len_penis(us.id)) + ' см'
                if us.id == '329341636574183424' :
                    baz = 'базука'
                if us.id == '307166488152899584':
                    toprol = 'хуесосить уебанов'
                ctrlstatus = str(us.status)
                OO = 0
                for OO in range(len(O)):
                    if O[OO][0] == (us) and ctrlstatus == 'offline':
                        ctrlstatus = 'invisible'
                        break
                gamedict = {'1': 'Стримит' , '2' : 'Слушает' , '3' : 'Смотрит' , '0' : 'Играет в'}
                s = 'Статус: {}\nСидит в воисе: {}\n{} {}\nАккаунт создан: {}\nПоследний раз перезаходил на сервер: {}\nКоэффициент активности: {}\nРазмер члена: {}\nВысшая роль: {}\nСписок всех ролей: {}'.format(statdict[ctrlstatus],us.voice.voice_channel,gamedict[str(us.game.type)] if us.game != None else 'Ни во что не играет' ,'**{}**'.format(us.game) if us.game != None else '',ltime2,ltime,aktkoef,baz,toprol,rols)
                embed=discord.Embed(description=s,color=col)
                embed.set_author(name=str(us), icon_url=us.avatar_url)
                embed.set_footer(text='ID: {}'.format(us.id))
                embed.set_thumbnail(url=us.avatar_url)
                try:
                    msg = await client.send_message(message.channel,embed=embed)
                except:
                    msg = await client.send_message(message.channel,'```{}\n\n{}```'.format(str(us),s))
                await delmes(msg)

client.loop.create_task(background())
client.loop.create_task(background2())
#client.run("zotic296@gmail.com","mcpe2359")
tr = 0
while True:
    try:
        tr +=1
        print("\x1b[32mПопытка входа №{}...\x1b[0m".format(tr))
        #client.connect()
        #client.login("zotic296@gmail.com","mcpe2359")
        #client.run("zotic296@gmail.com","mcpe2359")
        client.loop.run_until_complete(client.start("zotic296@gmail.com","mcpe2359"))
    except:
        print("\x1b[31mОшибка подключения, пытаюсь перезайти...\x1b[0m")

        client.logout()
        client.close()
        #client.loop.run_until_complete(client.logout())

        
#try:
 #   client.loop.run_until_complete(client.start("zotic296@gmail.com","mcpe2359"))
#except KeyboardInterrupt:
#    client.loop.run_until_complete(client.logout())
    # cancel all tasks lingering
#finally:
#    client.loop.close()
