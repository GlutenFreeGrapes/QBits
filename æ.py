import tkinter as tk,enchant
from tkinter import messagebox
ccccc=["Current Events", "Fine Arts", "Geography", "History", "Literature", "Mythology", "Philosophy", "Religion", "Science", "Social Science", "Trash"]
sssssccccc={"Current Events Subcategories":["American Current Events", "Other Current Events"], "Fine Arts Subcategories":["American Fine Arts", "Audiovisual Fine Arts", "Auditory Fine Arts", "British Fine Arts", "European Fine Arts", "Opera", "Visual Fine Arts", "World Fine Arts", "Other Fine Arts"], "Geography Subcategories":["American Geography", "World Geography"], "History Subcategories":["American History", "British History", "European History", "Classical History", "World History", "Other History"], "Literature Subcategories":["American Literature", "British Literature", "European Literature", "Classical Literature", "World Literature", "Other Literature"], "Mythology Subcategories":["American Mythology", "Chinese Mythology", "Egyptian Mythology", "Greco-Roman Mythology", "Indian Mythology", "Japanese Mythology", "Norse Mythology", "Other East Asian Mythology", "Other Mythology"], "Philosophy Subcategories":["American Philosophy", "Classical Philosophy", "East Asian Philosophy", "European Philosophy", "Other Philosophy"], "Religion Subcategories":["American Religion", "Christianity", "East Asian Religion", "Islam", "Judaism", "Other Religion"], "Science Subcategories":["American Science", "Biology", "Chemistry", "Computer Science", "Math", "Physics", "World Science", "Other Science"], "Social Science Subcategories":["American Social Science", "Anthropology", "Economics", "Linguistics", "Political Science", "Psychology", "Sociology", "Other Social Science"], "Trash Subcategories":["American Trash", "Movies", "Music", "Sports", "Television", "Video Games", "Other Trash"]}
ddddd=[str(i) for i in range(1,10)]
cc,sscc,dd,ttoouurr,ttbb,tthhyymmee=None,None,None,None,None,None
buzzed=False
reading=False
dead=False
ansalrgiven=False
qskipped=False
timeoutctr=None
endctr=None
qctr=None
tu=0
bon=0
ptn=[0,0,0]
bagels=[0,0,0,0]
tupts=0
bpts=0
tunum=-1
bonnum=-1
subbonnum=0
pm=0
curwd=0
tuct=None
tossuppts=None
ppg=None
ptnct=None
bonct=None
bonuspts=None
ppb=None
tttb=None
root=None
buzzer=None
curbpts=0
enterans=None
answerline=None
qcanvas=None
qtext=None
is_this_correct=None
tbrn=0
tulist=["""A leader of the fief of Kii who led the country during this period introduced sweet potato and sugarcane cultivation and began the compilation of the Kansei law code. Scholarly endeavors in this era were divided into the schools of Ancient Learning, National Learning, and Dutch Learning. This era included the artistic flourishing of the "original happiness period." Another ruler's attempt to stamp out Christianity during this era led to the (*)) Shimabara Rebellion. During the disintegration of its namesake government, this period saw the establishment of the Ezo Republic and the Boshin War. Ended by the proclamation of the Charter Oath and rallying behind Emperor Meiji, for 10 points, identify this final Japanese shogunate which lasted from 1600 to 1858.""", """Two wolves named "Greedy" and "Ravenous" devour the food that this deity doesn't eat. This deity can see far from his throne of Hlidskjalf, and has information brought to him by the ravens Huginn and Muninn. This deity hung on his spear Gungnir from the World Tree Yggdrasil in order to master the runes, and he gave up one of his eyes to drink from Mimir's well. He rides the eight-legged steed Sleipnir and will be swallowed whole by Fenrir at Ragnarok. For 10 points, name this owner of Valhalla, the chief god of the Norse pantheon.""","""A son of Zeus and Electra became one of the founders of this city after fleeing Samothrace whenZeus killed his brother Iasion. This city's territory was at one point divided between the brothers Ilusand Assaracus. A deceptive king of this city offered his daughter Hesione to a sea monster sent byPoseidon, who was angry because that king failed to (*) pay Poseidon and Apollo for building this city'swalls. Heracles sacked this city when he did not receive his promised immortal horses from Laomedon,who received those horses from Zeus as compensation for the rape of his brother, Ganymede. For 10points, name this Anatolian city ruled by Priam during a ten-year war with the Greeks."""]
tualist=["Tokugawa Shogunate","Odin","Troy [or Troia; or Ilium; or Ilion]"]
bonlist=[["""In 2013, this man was succeeded as Director of the FBI by James Comey, before being appointed to his current post by Deputy Attorney General Rod Rosenstein. For 10 points each:\nName this Republican Special Counsel for the Department of Justice, who is currently overseeing an investigation into Russian interference in the 2016 US Presidential Election.""", """This former Trump campaign advisor entered a plea deal with Mueller, which resulted in additional charges for him and Paul Manafort, such as conspiracy against the United States from when they lobbied for Ukraine.""","""Gates and Manafort were lobbyists for this pro-Russian Ukrainian Party. Former President Viktor Yanukovych was the first member of this party to be elected president before leaving office in 2014."""],["""In this text, a woman is impregnated by eating a lingonberry and gives birth to a son who becomes King of Karelia. For 10 points each:\nName this epic which contains the story of the virgin Marjatta. In another story from this epic, a comb begins to bleed after its hero drowns trying to capture a swan to win Louhi's daughter's hand in marriage.""","""The story of Marjatta symbolizes the Christianization of this European country, which reveres Ilmarinen and Väinämöinen as mythological heroes and regards the Kalevala as its national epic.""","""In Finland, the word for Satan, “saatana,” is frequently used as a swear word in conjunction with a word thought to refer to this chief Finnish god. This god of the sky conjured lightning from a hammer, axe or sword."""]]
bonalist=[["""Robert Mueller""", """Rick Gates""","""Party of Regions"""],["""Kalevala""","""Finland""","""Ukko"""]]

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + cx+self.widget.winfo_rootx()+self.widget.winfo_width()
        y = y + cy + self.widget.winfo_rooty()
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,background="#ffffe0", relief=tk.SOLID, borderwidth=1,font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
def handback(c,sc,d,tour,tb,tint):
    global cc,sscc,dd,ttoouurr,ttbb,tthhyymmee
    cc,sscc,dd,ttoouurr,ttbb,tthhyymmee=c,sc,d,tour,tb,tint
    return

def setup():
    root=tk.Tk()
    root.geometry("+20+20")
    root.title("yet another qb reader")
    fram1=tk.Frame(root)
    fram1.grid(row=0,column=0)
    cats=[tk.IntVar() for i in range(len(ccccc))]
    catl=tk.Label(fram1, text = 'Categories: ', font=('calibri',10, 'bold'))
    catt=tk.Menubutton (fram1, text="See options", relief=tk.RAISED)
    catt.menu =  tk.Menu (catt, tearoff = 0 )
    catt["menu"] = catt.menu
    for i in range(len(ccccc)):
        catt.menu.add_checkbutton(label=ccccc[i],variable=cats[i])
    lcats=tk.Button(fram1, text='❔')
    allsubcatlist=[]
    for i in sssssccccc:
        allsubcatlist.extend(sssssccccc[i])
    subcats=[tk.IntVar() for i in range(len(allsubcatlist))]
    subcatl=tk.Label(fram1, text = 'Subcategories: ', font=('calibri',10, 'bold'))
    subcatt=tk.Menubutton (fram1, text="See options", relief=tk.RAISED)
    subcatt.menu =  tk.Menu (subcatt, tearoff = 0 )
    subcatt["menu"] = subcatt.menu
    for n,i in enumerate(sorted(sssssccccc.keys())):
        subcatt.menu.add_command(label=i,state='disabled')
        for j in sssssccccc[i]:
            subcatt.menu.add_checkbutton(label=j,variable=subcats[allsubcatlist.index(j)])
    lsubcats=tk.Button(fram1, text='❔')
    diffs=[tk.IntVar() for i in range(len(ddddd))]
    diffl=tk.Label(fram1, text = 'Difficulties: ', font=('calibri',10, 'bold'))
    difft=tk.Menubutton (fram1, text="See options", relief=tk.RAISED)
    difft.menu =  tk.Menu (difft, tearoff = 0 )
    difft["menu"] = difft.menu
    for i in ddddd:
        difft.menu.add_checkbutton(label=i,variable=diffs[int(i)-1])
    ldiffs=tk.Button(fram1, text='❔')
    tours=tk.StringVar()
    tourl=tk.Label(fram1, text = 'Tournaments: ', font=('calibri',10, 'bold'))
    tourt=tk.Entry(fram1,textvariable = tours, font=('calibri',10,'normal'), width=50)
    ltours=tk.Button(fram1, text='❔')
    catl.grid(row=0,column=0, sticky="e")
    catt.grid(row=0,column=1)
    lcats.grid(row=0,column=2, sticky="w")
    CreateToolTip(lcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of categories: \n★ Current Events\n★ Fine Arts\n★ Geography\n★ History\n★ Literature\n★ Mythology\n★ Philosophy\n★ Religion\n★ Science\n★ Social Science\n★ Trash\n\nEx. \n"Current Events" → only gives questions from current events\n"History, Mythology, Science" → gives questions from history, mythology, and science')
    subcatl.grid(row=1,column=0, sticky="e")
    subcatt.grid(row=1,column=1)
    lsubcats.grid(row=1,column=2, sticky="w")
    CreateToolTip(lsubcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of subcategories: \n\n★ Current Events Subcategories: American Current Events, Other Current Events\n★ Fine Arts Subcategories: American Fine Arts, Audiovisual Fine Arts, \nAuditory Fine Arts, British Fine Arts, European Fine Arts, Opera, Visual Fine Arts, \nWorld Fine Arts, Other Fine Arts\n★ Geography Subcategories: American Geography, World Geography\n★ History Subcategories: American History, British History, European History, \nClassical History, World History, Other History\n★ Literature Subcategories: American Literature, British Literature, \nEuropean Literature, Classical Literature, World Literature, Other Literature\n★ Mythology Subcategories: American Mythology, Chinese Mythology, Egyptian Mythology, \nGreco-Roman Mythology, Indian Mythology, Japanese Mythology, Norse Mythology, \nOther East Asian Mythology, Other Mythology\n★ Philosophy Subcategories: American Philosophy, Classical Philosophy, \nEast Asian Philosophy, European Philosophy, Other Philosophy\n★ Religion Subcategories: American Religion, Christianity, East Asian Religion, \nIslam, Judaism, Other Religion\n★ Science Subcategories: American Science, Biology, Chemistry, Computer Science, \nMath, Physics, World Science, Other Science\n★ Social Science Subcategories: American Social Science, Anthropology, Economics, \nLinguistics, Political Science, Psychology, Sociology, Other Social Science\n★ Trash Subcategories: American Trash, Movies, Music, Sports, Television, \nVideo Games, Other Trash\n\nEx. \n"Greco-Roman Mythology, Computer Science" → only gives greco-roman mythology and \ncomputer science questions')
    diffl.grid(row=2,column=0, sticky="e")
    difft.grid(row=2,column=1)
    ldiffs.grid(row=2,column=2, sticky="w")
    CreateToolTip(ldiffs, text = 'Pick whatever question difficulty levels you want, separated by commas. Leave blank for all. \nBelow is a list of all the difficulty level numbers and the difficulties they correspond to: \n1 → Middle School\n2 → Easy High School\n3 → Regular High School\n4 → Hard High School\n5 → National High School\n6 → Easy College\n7 → Regular College\n8 → Hard College\n9 → Open\n\nEx. \n"6" → questions with easy college difficulty\n"4,5,6,7" → questions with difficulty ranging from hard high school to regular college')
    tourl.grid(row=3,column=0, sticky="e")
    tourt.grid(row=3,column=1, sticky="w")
    ltours.grid(row=3,column=2, sticky="w")
    CreateToolTip(ltours, text = 'Pick whatever tournaments you want, separated by commas. Leave blank for all. \nYou may enter either simply years or simply packet names. \n\nEx. \n"2020 pace" → 2020 PACE NSC packet\n"2020" → tournaments from 2020\n"pace" → all packets from PACE NSC tournaments')
    fram2=tk.Frame(root)
    fram2.grid(row=1,column=0)
    timeo=tk.Label(fram2, text = 'Time between each word (ms): ', font=('calibri',10, 'bold'))
    thyme = tk.Scale(fram2, from_=0, to=500, orient=tk.HORIZONTAL, length=400, tickinterval=50)
    thyme.set(250)
    timeex=tk.Button(fram2, text='❔')
    timeo.grid(row=0,column=0, sticky="e")
    thyme.grid(row=0,column=1, sticky="w")
    timeex.grid(row=0,column=2, sticky="w")
    CreateToolTip(timeex, text = 'Changes interval between words. Higher values mean longer intervals and thus \nthe question is read slower. Smaller values mean shorter intervals and thus \nthe words are read faster. ')
    fram3=tk.Frame(root)
    fram3.grid(row=2,column=0)
    tubon=tk.IntVar()
    tuorbon=tk.Label(fram3, text = 'What kind of questions do you want? ', font=('calibri',10, 'bold'))
    tu=tk.Radiobutton(fram3, text='Tossups only', variable=tubon, value=0)
    bon=tk.Radiobutton(fram3, text='Bonuses only', variable=tubon, value=1)
    tunbon=tk.Radiobutton(fram3, text='Tossups and bonuses', variable=tubon, value=2)
    tubonex=tk.Button(fram3, text='❔')
    def submit():
        c=[ccccc[i] for i in range(len(ccccc)) if cats[i].get()>0]
        if c==[]:
            c=ccccc
        sc=[allsubcatlist[i] for i in range(len(allsubcatlist)) if subcats[i].get()>0]
        d=[ddddd[i] for i in range(len(ddddd)) if diffs[i].get()>0]
        if d==[]:
            d=ddddd
        t=tours.get().strip().split(',')
        tb=tubon.get()
        tour=[i.strip().lower().replace(' ','') for i in t if i.strip()!='']
        tint=thyme.get()
        handback(c,sc,d,tour,tb,tint)
        root.destroy()
    fram4=tk.Frame(root)
    fram4.grid(row=3,column=0)
    abt=tk.Button(fram4,text = 'About')
    CreateToolTip(abt, text = "Hello, I'm GlutenFreeGrapes. I created this program in January 2022 \nas an all-in-one self-study tool. \n\n★★★★★Why this?★★★★★\nI made this because every quizbowl studying tool out there was either \na tossup reader or a bonus reader, but never both. So, I decided to try \nand make one myself. \n\n★★★★★Credits★★★★★\nThis was inspired by Kevin Kwok's Protobowl, Karan Gurazada's QuizBug, \nand Pratyush Jaishanker's pkbot. \nThis program uses QuizDB, which was developed by Raynor Kuang.\n\n★★★★★Contact★★★★★\nMy Github is @GlutenFreeGrapes. \nMy hsquizbowl forums username is GlutenFreeGrapes. ")
    contr=tk.Button(fram4,text = 'How to Play')
    CreateToolTip(contr, text = """When the program is run, you will be prompted with a screen asking for inputs on what categories you \nwant, difficulties, etc. Use the dropdown menus to select your options. There are also options for \nchanging the time interval between words and whether you want tossups only, bonuses only, or tossups \nand bonuses. When you hit the [Go] button, the windo should momentarily close out only for another \nto open. The screen should read "Press [Next/Skip] to start". Press the Next/Skip button, and the \nreading should start. As of now I have not bound keys to the buttons, so no hitting [space] to buzz \nor [enter] to submit your answer. At the bottom of the screen there should be several buttons(all \nshould be disabled except the [Next/Skip] button), a space to type answers in, and a large slider. \nThe slider allows you to live-adjust the speed at which the program reads you the questions. \n★Tossups - When you start the reading, the program will read the tossup one word at a time. The \n[Next/Skip] button stays enabled in case you want to skip tossups. The [Buzz] button will be enabled so \nthat you can buzz in, and when you do, it disables itself and the [Next/Skip] button, and enables the \ntext entry box, and a timer for 8 seconds. When you have finished typing, hit the [Enter] button(in the \nGUI, not on your keyboard) and the program should either display the tossup and the correct answer or \nprompt you with a message asking whether your provided answer was correct. Once this happens, you should \nsee that your number of tossups you've heard, number of tossup points, points per 20 tossups heard, and \nyour powers/10s/negs ratio will have updated. When you have run out of tossups, everything will be \ndisabled, but you will see your stats. \n★Bonuses - When you start the reading, the program will read the bonus one word at a time. The \n[Next/Skip] button stays enabled in case you want to skip entire bonuses. The [Buzz] button will be \ndisabled so that you cannot buzz in, but the text entry and [Enter] have been enabled so you can simply \ntype in as the question is being read and submit any time the bonus is being read. There will be a 10 \nsecond timer at the end when it reads each part of the bonus, in case you choose to answer after the \nquestion has finished. When you have finished typing, hit the [Enter] button(in the GUI, not on your \nkeyboard) and the program should either display the part of the bonus and the correct answer or prompt \nyou with a message asking whether your provided answer was correct. Each time you complete a part of the \nbonus it will display all the previous parts of that bonus above the current bonus. After you have \ncompleted all 3 parts of the bonus, you should see that your number of bonus you've heard, number of \nbonus points, points per bonus, and your 30s/20s/10s/0s ratio will have updated. When you have run out \nof bonuses, everything will be disabled, but you will see your stats. \n★Tossups and Bonuses - This option basically has the same functionality as tossups and bonuses, just \ncombined. I've made it such that even if you may have gotten a tossup wrong you will still be read a \nbonus after it, because I have the program simply alternate between tossups and bonuses. """)
    sumbit=tk.Button(fram4,text = 'Go', command = submit)
    quibt=tk.Button(fram4,text = 'Quit', command = quit)
    tuorbon.grid(row=0,column=0, sticky="e")
    tu.grid(row=0,column=1, sticky="w")
    bon.grid(row=0,column=2, sticky="w")
    tunbon.grid(row=0,column=3, sticky="w")
    tubonex.grid(row=0,column=4, sticky="w")
    CreateToolTip(tubonex, text = 'Tossups only → tk\nBonuses only → pk\nTossups and bonuses → basically a normal packet reading')
    abt.grid(row=0,column=0,padx=(0,10),pady=(0,5))
    contr.grid(row=0,column=1,padx=(10,10),pady=(0,5))
    sumbit.grid(row=0,column=2,padx=(10,10),pady=(0,5))
    quibt.grid(row=0,column=3,padx=(10,0),pady=(0,5))
    root.mainloop()
def qscreen(tuorbon,timeint):
    global buzzed,root,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct
    root=tk.Tk()
    root.geometry("+20+20")
    root.title('yet another qb reader')
    topf=tk.Frame(root)
    topf.grid(row=0,column=0)
    statframe=tk.LabelFrame(topf, text='Stats')
    statframe.grid(row=0,column=0)
    qframe=tk.Frame(root)
    qframe.grid(row=1,column=0)
    qcanvas=tk.Canvas(qframe,width=600,height=400,background="white")
    qcanvas.pack()
    qtext=qcanvas.create_text(int(qcanvas['width'])/2,int(qcanvas['height'])/2,text='Press [Next/Skip] to start', width=qcanvas['width'], fill="black",font=("times new roman", 15))
    bframe=tk.LabelFrame(root, text='Controls')
    bframe.grid(row=2,column=0)
    controlframe=tk.Frame(bframe)
    controlframe.grid(row=0,column=0)
    qbt=tk.Button(topf,text='Quit',command=quit)
    buzzed=False
    tuct=tk.Label(statframe,text='Tossups: %s'%(tu))
    tossuppts=tk.Label(statframe,text='Tossup Points: %s'%(tupts))
    ppg=tk.Label(statframe,text='PP20TUH: %s'%(0 if tu==0 else tupts/tu*20))
    ptnct=tk.Label(statframe,text='Powers/10s/Negs: %s'%('/'.join(str(i) for i in ptn)))
    bonct=tk.Label(statframe,text='Bonuses: %s'%(bon))
    bonuspts=tk.Label(statframe,text='Bonus Points: %s'%(bpts))
    ppb=tk.Label(statframe,text='PPB: %s'%(0 if bon==0 else bpts/bon))
    tttb=tk.Label(statframe,text='30s/20s/10s/0s: %s'%('/'.join(str(i) for i in bagels)))
    is_this_correct=tk.StringVar()
    answerline=tk.Entry(controlframe, textvariable = is_this_correct, width=30,state='disabled')
    def buzzin():
        global buzzed,timeoutctr
        buzzed=True
        answerline['state']='normal'
        enterans['state']='normal'
        buzzer['state']='disabled'
        read['state']='disabled'
        if endctr:
            qframe.after_cancel(endctr)
        answerline.focus_set()
        timeoutctr=root.after(8000,checkanswer)
    def prompt(gans,aans):
        if gans.strip()=='idk' or gans.strip()=='':
            return False
        return messagebox.askyesno("Were you correct?","Were you correct?\nYour answer: %s\nActual answer: %s"%(gans,aans))
    def checkanswer():
        global tu,tupts,bon,bpts,ptn,bagels,ansalrgiven,timeoutctr,reading,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,curbpts,tbrn
        if not ansalrgiven and not dead:
            if timeoutctr!=None:
                root.after_cancel(timeoutctr)
            if endctr!=None:
                qframe.after_cancel(endctr)
            givenans=is_this_correct.get()
            ansalrgiven=True
            answerline.delete(0,len(givenans))
            if tbrn==0:
                actualans=tualist[tunum]
                if buzzed:
                    if close_enough(givenans.lower(),actualans.lower()):
                        if curwd<=pm:
                            tupts+=15
                            ptn[0]+=1
                        else:
                            tupts+=10
                            ptn[1]+=1
                    else:
                        if reading:
                            if prompt(givenans,actualans):
                                if curwd<=pm:
                                    tupts+=15
                                    ptn[0]+=1
                                else:
                                    tupts+=10
                                    ptn[1]+=1
                            else:
                                tupts-=5
                                ptn[2]+=1
                        else:
                            if prompt(givenans,actualans):
                                if curwd<=pm:
                                    tupts+=15
                                    ptn[0]+=1
                                else:
                                    tupts+=10
                                    ptn[1]+=1
                    tu+=1
                    qcanvas.itemconfigure(qtext,text=tulist[tunum]+'\n\n'+tualist[tunum])
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    read['state']='normal'
                    reading=False
                    tuct['text']='Tossups: %s'%(tu)
                    tossuppts['text']='Tossup Points: %s'%(tupts)
                    ppg['text']='PP20TUH: %s'%(0 if tu==0 else tupts/tu*20)
                    ptnct['text']='Powers/10s/Negs: %s'%('/'.join(str(i) for i in ptn))
                    if tuorbon==2:
                        tbrn=1-tbrn
                    root.update()
            else:
                answerline['state']='disabled'
                enterans['state']='disabled'
                actualans=bonalist[bonnum][subbonnum]
                if close_enough(givenans.lower(),actualans.lower()):
                    curbpts+=10
                else:
                    if prompt(givenans,actualans):
                        curbpts+=10
                    else:
                        curbpts+=0
                reading=False
                aread=bonlist[bonnum][:subbonnum]
                allread=''
                for n,i in enumerate(aread):
                    allread+=i
                    allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
                qcanvas.itemconfigure(qtext,text=allread+bonlist[bonnum][subbonnum]+"\n\n"+bonalist[bonnum][subbonnum])
                read['state']='normal'
                if subbonnum==2:
                    bon+=1
                    bpts+=curbpts
                    bagels[(30-curbpts)//10]+=1
                    bonct['text']='Bonuses: %s'%(bon)
                    bonuspts['text']='Bonus Points: %s'%(bpts)
                    ppb['text']='PPB: %s'%(0 if bon==0 else bpts/bon)
                    tttb['text']='30s/20s/10s/0s: %s'%('/'.join(str(i) for i in bagels))
                    root.update()
                    if tuorbon==2:
                        tbrn=1-tbrn
    enterans=tk.Button(controlframe,text="Enter",command=checkanswer,state='disabled')
    enterans.grid(row=0,column=4)
    buzzer=tk.Button(controlframe,text="Buzz",command=buzzin)
    if reading==False:
        buzzer['state']='disabled'
    tcframe=tk.Frame(bframe)
    tcframe.grid(row=2,column=0)
    timeo=tk.Label(tcframe, text = 'Time between each word (ms): ', font=('calibri',10, 'bold'))
    thyme = tk.Scale(tcframe, from_=0, to=500, orient=tk.HORIZONTAL, length=400, tickinterval=50)
    thyme.set(timeint)
    timeo.grid(row=0,column=0)
    thyme.grid(row=0,column=1)
    def readq():
        global reading,buzzed,tunum,dead,ansalrgiven,qskipped,bonnum,subbonnum,curbpts
        if not reading:
            reading=True
            buzzed=False
            dead=False
            ansalrgiven=False
            qskipped=False
            if tuorbon==0 or (tuorbon==2 and tbrn==0):
                tunum+=1
            else:
                if subbonnum==2 or bonnum<0:
                    bonnum+=1
                    subbonnum=0
                    curbpts=0
                else:
                    subbonnum+=1
            if tuorbon==0:
                if tunum>=len(tulist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    return
                if reading and tbrn==0:
                    buzzer['state']='normal'
                qcanvas.itemconfigure(qtext, font=("times new roman", 15))
                read_tossup(qframe,qcanvas,qtext,thyme)
            elif tuorbon==1:
                if bonnum>=len(bonlist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    return
                if reading and tbrn==1:
                    buzzer['state']='disabled'
                    answerline['state']='normal'
                    enterans['state']='normal'
                qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                answerline.focus_set()
                read_bonus(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    if tunum>=len(tulist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        return
                    if reading and tbrn==0:
                        buzzer['state']='normal'
                    qcanvas.itemconfigure(qtext, font=("times new roman", 15))
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    if reading and tbrn==1:
                        buzzer['state']='disabled'
                        answerline['state']='normal'
                        enterans['state']='normal'
                    qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                    answerline.focus_set()
                    read_bonus(qframe,qcanvas,qtext,thyme)
        else:
            qskipped=True
            if qctr:
                qframe.after_cancel(qctr)
            if endctr:
                qframe.after_cancel(endctr)
            if timeoutctr:
                root.after_cancel(timeoutctr)
            qskipped=False
            if tuorbon==0:
                tunum+=1
                if tunum>=len(tulist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    return
                read_tossup(qframe,qcanvas,qtext,thyme)
            elif tuorbon==1:
                bonnum+=1
                subbonnum=0
                curbpts=0
                if bonnum>=len(bonlist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    return
                answerline.focus_set()
                read_bonus(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    tunum+=1
                    if tunum>=len(tulist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        return
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    bonnum+=1
                    subbonnum=0
                    curbpts=0
                    if bonnum>=len(bonlist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        return
                    answerline.focus_set()
                    read_bonus(qframe,qcanvas,qtext,thyme)
    read=tk.Button(controlframe,text="Next/Skip",command=readq)
    read.grid(row=0,column=0)
    if tuorbon==0:
        tuct.grid(row=0,column=0)
        tossuppts.grid(row=0,column=1)
        ppg.grid(row=0,column=2)
        ptnct.grid(row=0,column=3)
    elif tuorbon==1:
        bonct.grid(row=0,column=0)
        bonuspts.grid(row=0,column=1)
        ppb.grid(row=0,column=2)
        tttb.grid(row=0,column=3)
    else:
        tuct.grid(row=0,column=0)
        tossuppts.grid(row=0,column=1)
        ppg.grid(row=0,column=2)
        ptnct.grid(row=0,column=3)
        bonct.grid(row=1,column=0)
        bonuspts.grid(row=1,column=1)
        ppb.grid(row=1,column=2)
        tttb.grid(row=1,column=3)
    answerline.grid(row=0,column=3)
    buzzer.grid(row=0,column=2)
    qbt.grid(row=0,column=1,sticky='e')
    root.mainloop()
def close_enough(str1,str2):
    dna=str2.find("[")
    if dna<0:
        dna=str2.find("do not accept")
        if dna<0:
            dna=str2.find('<')
    if dna<0:
        if enchant.utils.levenshtein(str1,str2)<len(str2)/2:
            return True
    else:
        s=str2[:dna]
        if enchant.utils.levenshtein(s,str1)<len(s)/2:
            return True
    return False
def check_if_buzz_at_eotu():
    global dead,tu,tuct,tossuppts,ppg,ptnct,root,buzzer,qcanvas,qtext
    if reading==False and buzzed==False:
        dead=True
        tu+=1
        qcanvas.itemconfigure(qtext,text=tulist[tunum]+'\n\n'+tualist[tunum])
        tuct['text']='Tossups: %s'%(tu)
        ppg['text']='PP20TUH: %s'%(0 if tu==0 else tupts/tu*20)
        buzzer['state']='disabled'
        root.update()
def check_if_buzz_at_eobon():
    global dead,bon,bonct,bonuspts,ppb,tttb,curbpts,answerline
    ans=is_this_correct.get()
    if ans!="":
        answerline.delete(0,len(ans))
        if close_enough(ans,bonalist[bonnum][subbonnum]):
            curbpts+=10
    if reading==False and ansalrgiven==False:
        dead=True
        answerline['state']='disabled'
        enterans['state']='disabled'
        aread=bonlist[bonnum][:subbonnum]
        allread=''
        for n,i in enumerate(aread):
            allread+=i
            allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
        qcanvas.itemconfigure(qtext,text=allread+bonlist[bonnum][subbonnum]+"\n\n"+bonalist[bonnum][subbonnum])
def read_tossup(window,canvas,question_txt,timeint):
    global pm
    current_q = tulist[tunum]
    powermark=current_q.find("(*)")
    words=current_q.split()
    if powermark>-1:
        index=current_q[:powermark].count(" ")
        pm=index
        words.pop(index)
        words[index-1]+=" (*)"
    else:
        pm=-1
    itertu(words, 0, window,canvas,question_txt,timeint)
def itertu(words, i, window,canvas,question_txt,timeint):
    global curwd,qctr
    curwd=i-1
    if i > len(words):
        global reading,endctr
        reading=False
        endctr=window.after(5000,check_if_buzz_at_eotu)
        return
    if qskipped:
        return
    if not buzzed:
        canvas.itemconfigure(question_txt, text=' '.join(words[:i]))
        i += 1
        qctr = window.after(timeint.get(), lambda: itertu(words, i,window,canvas,question_txt,timeint))
def read_bonus(window,canvas,question_txt,timeint):
    current_q = bonlist[bonnum]
    bonwords=current_q[subbonnum].split()
    if subbonnum==0:
        breakspace=current_q[subbonnum][:current_q[subbonnum].find("\n")].count(' ')
        if breakspace>=0:
            bonwords[breakspace+1]='\n'+bonwords[breakspace+1]
    aread = current_q[:subbonnum]
    allread=''
    for n,i in enumerate(aread):
        allread+=i
        allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
    iterbon(allread,bonwords, 0, window,canvas,question_txt,timeint)
def iterbon(allread, words, i, window,canvas,question_txt,timeint):
    if i > len(words):
        global reading,endctr,qctr
        reading=False
        endctr=window.after(10000,check_if_buzz_at_eobon)
        return
    if qskipped:
        return
    if not ansalrgiven:
        canvas.itemconfigure(question_txt, text=allread+' '.join(words[:i]))
        i += 1
        qctr = window.after(timeint.get(), lambda: iterbon(allread,words, i,window,canvas,question_txt,timeint))
setup()
if (cc,sscc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None,None):
    if ttbb<2:
        tbrn=ttbb
    else:
        tbrn=0
    qscreen(ttbb,tthhyymmee)
#turn tournaments option into a dropdown sometime when granted access to quizdb db