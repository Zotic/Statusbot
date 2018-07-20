import discord
import asyncio
import random

client = discord.Client()



global info
info = False
global check
check = False
global kod
kod = 0
global chan
global winner
global pop
pop = 0
global uslist
uslist = []
global us
us = 0



@client.event
async def on_ready():
    print ("Bomba v.5.0 активирована")
    print ("Имя: {}".format(client.user.name))
    print ("ID: {}".format(client.user.id))
    print ("____________________________")



async def otschet(msg1,kol,maxk,q1,chan,ran):
    bum = True
    global pop
    global check
    global kod
    kol2 = kol
    s1 =''
    s2 = ''
    k = 0
    k2 = 0
    car = ''
    qq = 1
    if q1 == 0:
        q1 = 99999999999999999999999
        qq = 0
    for i in range(kol):
        k2 = k2+1
        k = k+1
         
        if check:
            bum = False
            
            break
        
        else:
            q = q1 - pop
            if q < 1:
                bum = True
                break
            else:
                s1 =''
                s2 = ''
                embed=discord.Embed(title="Бомба заложена!", description="Чтобы разминировать бомбу ведите число от 1 до "+str(maxk), color=0xff0000)
                embed.set_thumbnail(url='https://vignette3.wikia.nocookie.net/counterstrike/images/a/aa/W_c4_csgo-1-.png/revision/latest?cb=20160502165335&path-prefix=ru')
                sk1 = round(41/100*(100 / kol2 * (kol-i)))
                sk2 = round(41/100*(100 / q1 * q))
                for ppp in range(38):  
                    if ppp <= sk1:
                        s1 = s1+'█'
                    else:
                        s1 = s1+"▒"
                    if ppp <= sk2:
                        s2 = s2+'█'
                    else:
                        s2 = s2+"▒"
                embed.add_field(name="До взрыва секунд: {}".format(kol-i), value=s1, inline=False)
                if qq!=0:
                    embed.add_field(name="Попыток: {}".format(q), value=s2, inline=False)
                if k2 == ran:
                    k2 = 0
                    kod = random.randint(1,maxk)
                    print (str(kod))  
                if ran > 0:
                    embed.add_field(name="Внимание, код меняется! Интервал в секундах: ", value=str(ran), inline=True)
                embed.set_footer(text="Если бомба взорвется, один из тех, кто принимал участие в разминировании выживет!")

                #text = "До взрыва осталось секунд: "+str(kol-i)+"\nЧтобы разминировать введите код от 1 до "+str(maxk)+"\nОсталось попыток: "+str(q)

                if k == 10:
                    k = 0
                    await client.delete_message(msg1)
                    msg1 = await client.send_message(chan,embed=embed)


                else:
                    await client.edit_message(msg1,embed=embed)
        await asyncio.sleep(1)  
    if bum:
        await client.delete_message(msg1)
    return(bum)


@client.event
async def on_message(message):
    global pop
    global maxk
    global check
    global uslist
    global us
    global kod
    if message.author.id == client.user.id:
        if message.content.startswith("Help"):
            embed=discord.Embed(title="Гайд по бомбе", description="Чтобы разминировать бомбу ведите число от 1 до {2=макс рандома}", color=0xffff00)
            embed.add_field(name="До взрыва секунд: {1=время}" , value="██████████████████████████████████████████████", inline=False)
            embed.add_field(name="Попыток: {3=попытки,0}" , value="██████████████████████████████████████████████", inline=False)
            embed.add_field(name="Внимание, код меняется! Интервал в секундах:", value="{4=интервал,0}", inline=True)
            embed.set_footer(text="Start 1 2 3 4")
            await client.edit_message(message,'Гайд по бомбе',embed=embed)
        if message.content.startswith("Start"):
            uslist = ['','','']
            us = 0
            print ("Принято")
            global chan
            msgg = str(message.content)
            msgg = msgg[msgg.find(' ')+1:len(msgg)]
            kol = int(msgg[:msgg.find(' ')+1])
            msgg = msgg[msgg.find(' ')+1:len(msgg)]
            maxk = int(msgg[:msgg.find(' ')+1])
            msgg = msgg[msgg.find(' ')+1:len(msgg)]
            q1 = int(msgg[:msgg.find(' ')+1])
            msgg = msgg[msgg.find(' ')+1:len(msgg)]
            ran = int(msgg)
            msg = message
            chan = msg.channel      
           # maxk = 1000
            #q1 = 25000
            await client.edit_message(msg,"Бомба заложена!")

            kod = random.randint(1,maxk)
            print ("Код: "+str(kod))
            global info
            info = True        
            #await otschet(msg,kol,q)
            global winner
            ma = message.author
            if await otschet(msg,kol,maxk,q1,chan,ran):
                
                await client.send_message(chan,"БУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУМ\nБУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУМ\nБУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУМ")
                await client.send_file(chan, 'vzriv.png')
                if us == 0:
                    us = 1 
                    uslist.append('')
                    uslist[1]= ma
                    win = 1
                else:
                    win = random.randint(1,us)
                embed2=discord.Embed(title="Буууууууууууууууууууууууууууууум", description="Завода больше нет!", color=0x0b0b0b)
                embed2.set_thumbnail(url='http://old.bryanskobl.ru/region/history/img/bmz_ruines_b.jpg')
                embed2.add_field(name="Код от бомбы был: ", value=str(kod), inline=True)
                embed2.add_field(name="Саперов было: ", value=str(us), inline=True)
                embed2.add_field(name="Единственный выживший: ", value="{0.mention}".format(uslist[win]), inline=True)
                await client.send_message(chan,embed=embed2)
                #await client.send_message(chan,"Код от бомбы был: "+ str(kod) + "\nВ разминировании приняло участие человек: "+str(us)+"\nЕдинственный выживший: {0.mention}".format(uslist[win]))
            else:
                embed3=discord.Embed(title="Завод спасен!", description= "{0.author.mention} разминировал бомбу!".format(winner),color=0x00ff00)
                embed3.set_author(name=winner.author.name + " разминировал бомбу!", icon_url=winner.author.avatar_url)
                embed3.set_thumbnail(url="http://vesti.lv/upload/picture/picture/2016_11/358903/1480290453-new_article.jpg?1479662226")
                embed3.add_field(name="Код от бомбы был:", value=str(kod), inline=True)
                embed3.add_field(name="Саперов участвовало: ", value=str(us), inline=True)
                #await client.send_message(chan,"{0.author.mention} разминировал бомбу!\n{0.author.mention} разминировал бомбу!\n{0.author.mention} разминировал бомбу!\n{0.author.mention} разминировал бомбу!\n{0.author.mention} разминировал бомбу!".format(winner))
                await client.send_message(chan,embed=embed3)
            check = False
            info = False  
            uslist = []
            pop = 0
            print("____________________________")
    if info:
        if message.channel == chan:
            try:
                int(message.content)
            except ValueError:
                pass
            else:
                if int(message.content) == kod:
                    check = True
                    winner = message
                    if us == 0:
                        us = us+1
                    info = False
                    
    
                else:
                    if (int(message.content) < maxk+1) and (int(message.content)>0):
                        pop = pop +1
                        chlist = False
                        if us == 0:
                            pass
                        else:
                            for l in range(us+1):

                                if uslist[l] == message.author:
                                    chlist = True
                        if chlist == False:
                            us = us+1
                            uslist.append('')
                            uslist[us] = message.author

                    




client.run("zotic296@gmail.com","mcpe2359")
