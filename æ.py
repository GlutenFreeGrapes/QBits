import tkinter as tk,enchant,random,json,bs4
from tkinter import messagebox
ccccc=["Current Events", "Fine Arts", "Geography", "History", "Literature", "Mythology", "Philosophy", "Religion", "Science", "Social Science", "Trash"]
sssssccccc={"Current Events Subcategories":["American Current Events", "Other Current Events"], "Fine Arts Subcategories":["American Fine Arts", "Audiovisual Fine Arts", "Auditory Fine Arts", "British Fine Arts", "European Fine Arts", "Opera", "Visual Fine Arts", "World Fine Arts", "Other Fine Arts"], "Geography Subcategories":["American Geography", "World Geography"], "History Subcategories":["American History", "British History", "Classical History", "European History", "World History", "Other History"], "Literature Subcategories":["American Literature", "British Literature", "Classical Literature", "European Literature", "World Literature", "Other Literature"], "Mythology Subcategories":["American Mythology", "Chinese Mythology", "Egyptian Mythology", "Greco-Roman Mythology", "Indian Mythology", "Japanese Mythology", "Norse Mythology", "Other East Asian Mythology", "Other Mythology"], "Philosophy Subcategories":["American Philosophy", "Classical Philosophy", "East Asian Philosophy", "European Philosophy", "Other Philosophy"], "Religion Subcategories":["American Religion", "Christianity", "East Asian Religion", "Islam", "Judaism", "Other Religion"], "Science Subcategories":["American Science", "Biology", "Chemistry", "Computer Science", "Math", "Physics", "World Science", "Other Science"], "Social Science Subcategories":["American Social Science", "Anthropology", "Economics", "Linguistics", "Political Science", "Psychology", "Sociology", "Other Social Science"], "Trash Subcategories":["American Trash", "Movies", "Music", "Sports", "Television", "Video Games", "Other Trash"]}
ddddd=list(range(1,10))
tttttooooouuuuurrrrr,tourids=dict(),dict()
cc,sscc,dd,ttoouurr,ttbb,tthhyymmee,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,root,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct,timeoutctr,endctr,qctr=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
buzzed,reading,dead,ansalrgiven,qskipped=False,False,False,False,False
ptn,bagels=[0,0,0],[0,0,0,0]
tu,bon,tupts,bpts,tunum,bonnum,subbonnum,pm,curwd,curbpts,tbrn=0,0,0,0,-1,-1,0,0,0,0,0
tulist,tualist,tufalist,bonlist,bonalist,bonfalist=[],[],[],[],[],[]
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
def settourlist():
    global tourids,tttttooooouuuuurrrrr
    with open('quizdb-20220122021550.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in ddddd:
        tttttooooouuuuurrrrr["Difficulty Level %s"%i]=set()
    for j in data["data"]["tossups"],data["data"]["bonuses"]:
        for i in j:
            if i["tournament_id"]:
                if i["tournament"]["name"] not in tourids:
                    tourids[i["tournament"]["name"]]=i["tournament_id"]
                if i["tournament"]["difficulty_num"] in tttttooooouuuuurrrrr:
                    tttttooooouuuuurrrrr["Difficulty Level %s"%i["tournament"]["difficulty_num"]].add(i["tournament"]["name"])
                else:
                    tttttooooouuuuurrrrr["Difficulty Level %s"%i["tournament"]["difficulty_num"]]={i["tournament"]["name"]}
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
    alltourlist=[]
    for i in tttttooooouuuuurrrrr:
        alltourlist.extend(tttttooooouuuuurrrrr[i])
    tours=[tk.IntVar() for i in range(len(alltourlist))]
    tourl=tk.Label(fram1, text = 'Tournaments: ', font=('calibri',10, 'bold'))
    tourt=tk.Menubutton (fram1, text="See options", relief=tk.RAISED)
    tourt.menu =  tk.Menu (tourt, tearoff = 0 )
    tourt["menu"] = tourt.menu
    for n,i in enumerate(sorted(tttttooooouuuuurrrrr.keys())):
        tourt.menu.add_command(label=i,state='disabled')
        for j in tttttooooouuuuurrrrr[i]:
            tourt.menu.add_checkbutton(label=j,variable=tours[alltourlist.index(j)])
    ltours=tk.Button(fram1, text='❔')
    catl.grid(row=0,column=0, sticky="e")
    catt.grid(row=0,column=1)
    lcats.grid(row=0,column=2, sticky="w")
    CreateToolTip(lcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of categories: \n★ Current Events\n★ Fine Arts\n★ Geography\n★ History\n★ Literature\n★ Mythology\n★ Philosophy\n★ Religion\n★ Science\n★ Social Science\n★ Trash\n\nEx. \n"Current Events" → only gives questions from current events\n"History, Mythology, Science" → gives questions from history, mythology, and science\n"Geography", "Video Games" in subcategories → any questions on geography, \nalong with video game questions')
    subcatl.grid(row=1,column=0, sticky="e")
    subcatt.grid(row=1,column=1)
    lsubcats.grid(row=1,column=2, sticky="w")
    CreateToolTip(lsubcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of subcategories: \n\n★ Current Events Subcategories: American Current Events, Other Current Events\n★ Fine Arts Subcategories: American Fine Arts, Audiovisual Fine Arts, \nAuditory Fine Arts, British Fine Arts, European Fine Arts, Opera, Visual Fine Arts, \nWorld Fine Arts, Other Fine Arts\n★ Geography Subcategories: American Geography, World Geography\n★ History Subcategories: American History, British History, European History, \nClassical History, World History, Other History\n★ Literature Subcategories: American Literature, British Literature, \nEuropean Literature, Classical Literature, World Literature, Other Literature\n★ Mythology Subcategories: American Mythology, Chinese Mythology, Egyptian Mythology, \nGreco-Roman Mythology, Indian Mythology, Japanese Mythology, Norse Mythology, \nOther East Asian Mythology, Other Mythology\n★ Philosophy Subcategories: American Philosophy, Classical Philosophy, \nEast Asian Philosophy, European Philosophy, Other Philosophy\n★ Religion Subcategories: American Religion, Christianity, East Asian Religion, \nIslam, Judaism, Other Religion\n★ Science Subcategories: American Science, Biology, Chemistry, Computer Science, \nMath, Physics, World Science, Other Science\n★ Social Science Subcategories: American Social Science, Anthropology, Economics, \nLinguistics, Political Science, Psychology, Sociology, Other Social Science\n★ Trash Subcategories: American Trash, Movies, Music, Sports, Television, \nVideo Games, Other Trash\n\nEx. \n"Greco-Roman Mythology, Computer Science" → only gives greco-roman mythology and \ncomputer science questions\n"Physics", "Literature" in categories → any questions on physics, along with literature\n questions')
    diffl.grid(row=2,column=0, sticky="e")
    difft.grid(row=2,column=1)
    ldiffs.grid(row=2,column=2, sticky="w")
    CreateToolTip(ldiffs, text = 'Pick whatever question difficulty levels you want, separated by commas. Leave blank for all. \nBelow is a list of all the difficulty level numbers and the difficulties they correspond to: \n1 → Middle School\n2 → Easy High School\n3 → Regular High School\n4 → Hard High School\n5 → National High School\n6 → Easy College\n7 → Regular College\n8 → Hard College\n9 → Open\n\nEx. \n"6" → questions with easy college difficulty\n"4,5,6,7" → questions with difficulty ranging from hard high school to regular college\n"6", "2020 Oxford Online" in tournaments → any questions in difficulty level 6\n along with questions from 2020 Oxford Online packet')
    tourl.grid(row=3,column=0, sticky="e")
    tourt.grid(row=3,column=1)
    ltours.grid(row=3,column=2, sticky="w")
    CreateToolTip(ltours, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \n\nEx. \n"2020 CALISTO" → 2020 CALISTO packet, along with whatever \ndifficulty levels you have selected\n"2020 CALISTO, 2020 Terrapin", selected "6" in difficulty level → 2020 CALISTO and \n2020 Terrapin, along with any questions with diffuculty level 6')
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
        t=[alltourlist[i] for i in range(len(alltourlist)) if tours[i].get()>0]
        if d==[] and t==[]:
            d=ddddd
        tb=tubon.get()
        tint=thyme.get()
        handback(c,sc,d,t,tb,tint)
        root.destroy()
    fram4=tk.Frame(root)
    fram4.grid(row=3,column=0)
    abt=tk.Button(fram4,text = 'About')
    CreateToolTip(abt, text = "Hello, I'm GlutenFreeGrapes. I created this program in January 2022 \nas an all-in-one self-study tool. \n\n★★★★★Why this?★★★★★\nI made this because every quizbowl studying tool out there was either \na tossup reader or a bonus reader, but never both. So, I decided to try \nand make one myself. \n\n★★★★★Credits★★★★★\nThis was inspired by Kevin Kwok's Protobowl, Karan Gurazada's QuizBug, \nand Pratyush Jaishanker's pkbot. \nThis program uses QuizDB, which was developed by Raynor Kuang.\n\n★★★★★Contact★★★★★\nMy Github is @GlutenFreeGrapes. \nMy hsquizbowl forums username is GlutenFreeGrapes. ")
    contr=tk.Button(fram4,text = 'Controls')
    CreateToolTip(contr, text = """Keybinds:\n] → [Next/Skip]\nSpace → [Buzz]\nEnter → [Enter]\nEscape → [Quit]\n\nWhen the question starts, you will be able to live-adjust the time interval between words. \nDuring bonuses, the buzzer button should be disabled to prevent accidental buzzing during \nthem. You should be able to see your stats at the top of the window. """)
    sumbit=tk.Button(fram4,text = 'Go', command = submit)
    quibt=tk.Button(fram4,text = 'Quit', command = quit)
    root.bind('<Return>',lambda event:submit())
    root.bind('<Escape>',lambda event:quit())
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
    qtext=qcanvas.create_text(int(qcanvas['width'])/2,int(qcanvas['height'])/2,text='Press [Next/Skip] to start', width=qcanvas['width'], fill="black",font=("times new roman", 13))
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
    def buzzin():
        global buzzed,timeoutctr,root,enterans
        root.unbind("<space>")        
        buzzed=True
        answerline['state']='normal'
        enterans['state']='normal'
        root.bind("<Return>", lambda event: checkanswer())
        buzzer['state']='disabled'
        root.unbind("<space>")
        read['state']='disabled'
        root.unbind('<]>')
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
            root.unbind("<Return>")
            if timeoutctr!=None:
                root.after_cancel(timeoutctr)
            if endctr!=None:
                qframe.after_cancel(endctr)
            givenans=is_this_correct.get()
            ansalrgiven=True
            answerline.delete(0,len(givenans))
            if tbrn==0:
                fans=tufalist[tunum]
                actualans=tualist[tunum]
                if buzzed:
                    if close_enough(givenans.lower(),fans,actualans):
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
                    root.unbind("<Return>")
                    read['state']='normal'
                    root.bind('<]>', lambda event: readq())
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
                root.unbind("<Return>")
                fans=bonfalist[bonnum][subbonnum]
                actualans=bonalist[bonnum][subbonnum]
                if close_enough(givenans.lower(),fans,actualans):
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
                root.bind('<]>', lambda event: readq())
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
    answerline=tk.Entry(controlframe, textvariable = is_this_correct, width=30,state='disabled')
    enterans=tk.Button(controlframe,text="Enter",command=checkanswer,state='disabled')
    enterans.grid(row=0,column=4)
    buzzer=tk.Button(controlframe,text="Buzz",command=buzzin)
    if reading==False:
        buzzer['state']='disabled'
        root.unbind("<space>")
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
                    root.unbind('<]>')
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                if reading and tbrn==0:
                    buzzer['state']='normal'
                    root.bind("<space>", lambda event: buzzin())
                qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                read_tossup(qframe,qcanvas,qtext,thyme)
            elif tuorbon==1:
                if bonnum>=len(bonlist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    root.unbind('<]>')
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                if reading and tbrn==1:
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='normal'
                    enterans['state']='normal'
                    root.bind("<Return>", lambda event: checkanswer())
                qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                answerline.focus_set()
                read_bonus(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    if tunum>=len(tulist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        root.unbind('<]>')
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    if reading and tbrn==0:
                        buzzer['state']='normal'
                        root.bind("<space>", lambda event: buzzin())
                    qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    if reading and tbrn==1:
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='normal'
                        enterans['state']='normal'
                        root.bind("<Return>", lambda event: checkanswer())
                    qcanvas.itemconfigure(qtext, font=("times new roman", 13))
                    answerline.focus_set()
                    read_bonus(qframe,qcanvas,qtext,thyme)
        else:
            answerline.delete(0,len(is_this_correct.get()))
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
                    root.unbind('<]>')
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                read_tossup(qframe,qcanvas,qtext,thyme)
            elif tuorbon==1:
                bonnum+=1
                subbonnum=0
                curbpts=0
                if bonnum>=len(bonlist):
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                    read['state']='disabled'
                    root.unbind('<]>')
                    thyme['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                answerline.focus_set()
                read_bonus(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    tunum+=1
                    if tunum>=len(tulist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        root.unbind('<]>')
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    bonnum+=1
                    subbonnum=0
                    curbpts=0
                    if bonnum>=len(bonlist):
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Quit] to exit")
                        read['state']='disabled'
                        root.unbind('<]>')
                        thyme['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    answerline.focus_set()
                    read_bonus(qframe,qcanvas,qtext,thyme)
    read=tk.Button(controlframe,text="Next/Skip",command=readq)
    root.bind('<]>', lambda event: readq())
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
    root.bind('<Escape>',lambda event:quit())
    root.focus_force()
    root.mainloop()
def close_enough(given,htmlans,normalans):
    accepans=set()
    s=bs4.BeautifulSoup(htmlans, features="html.parser")
    strongs=s.find_all("strong")
    for i in strongs:
        accepans.add(i.string.lower())
    bs=s.find_all("b")
    for i in bs:
        accepans.add(i.string.lower())
    for i in accepans:
        if enchant.utils.levenshtein(given,i)<min(3,len(i)//2):
            return True
    dna=normalans.find("[")
    if dna<0:
        dna=normalans.find("(")
        if dna<0:
            dna=normalans.find("do not accept")
    if dna<0:
        if enchant.utils.levenshtein(given,normalans)<min(3,len(normalans)//2):
            return True
    else:
        s=normalans[:dna]
        if enchant.utils.levenshtein(s,given)<min(3,len(normalans)//2):
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
        root.unbind("<space>")
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
        root.unbind("<Return>")
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
def fetchqs(cats,subcats,diffs,tours,tuorbon):
    global tulist,tualist,tufalist,bonlist,bonalist,bonfalist
    catids={"Current Events":26, "Fine Arts":21, "Geography":20, "History":18, "Literature":15, "Mythology":14, "Philosophy":25, "Religion":19, "Science":17, "Social Science":22, "Trash":16}
    subcatids={'American Current Events':40, 'Other Current Events':42, 'American Fine Arts':35, 'Audiovisual Fine Arts':27, 'Auditory Fine Arts':8, 'British Fine Arts':45, 'European Fine Arts':50, 'Opera':77, 'Visual Fine Arts':2, 'World Fine Arts':43, 'Other Fine Arts':25, 'American Geography':38, 'World Geography':44, 'American History':13, 'British History':6, 'Classical History':16, 'European History':24, 'World History':20, 'Other History':28, 'American Literature':4, 'British Literature':22, 'Classical Literature':30, 'European Literature':1, 'World Literature':12, 'Other Literature':29, 'American Mythology':33, 'Chinese Mythology':47, 'Egyptian Mythology':65, 'Greco-Roman Mythology':58, 'Indian Mythology':46, 'Japanese Mythology':48, 'Norse Mythology':63, 'Other East Asian Mythology':49, 'Other Mythology':54, 'American Philosophy':39, 'Classical Philosophy':61, 'East Asian Philosophy':52, 'European Philosophy':66, 'Other Philosophy':74, 'American Religion':31, 'Christianity':57, 'East Asian Religion':51, 'Islam':68, 'Judaism':69, 'Other Religion':62, 'American Science':36, 'Biology':14, 'Chemistry':5, 'Computer Science':23, 'Math':26, 'Physics':18, 'World Science':37, 'Other Science':10, 'American Social Science':34, 'Anthropology':76, 'Economics':56, 'Linguistics':75, 'Political Science':64, 'Psychology':71, 'Sociology':73, 'Other Social Science':60, 'American Trash':32, 'Movies':72, 'Music':67, 'Sports':55, 'Television':70, 'Video Games':53, 'Other Trash':59}
    clist=set()
    sclist=set()
    dlist=set(diffs)
    tlist=set()
    for i in cats:
        clist.add(catids[i])
    for i in subcats:
        sclist.add(subcatids[i])
    for i in tours:
        tlist.add(tourids[i])
    with open('quizdb-20220122021550.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    if tuorbon==0 or tuorbon==2:
        for i in data["data"]["tossups"]:
            if i["text"]!="[missing]" and i["answer"]!="[missing]" and i["tournament_id"]:
                if (i["category_id"] in clist or i["subcategory_id"] in sclist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist):
                    tulist.append(i["text"])
                    a=i["answer"]
                    if a.find("&lt")>=0:
                        a=a[:a.find("&lt")]
                    elif a.find("<")>=0:
                        a=a[:a.find("<")]
                    tualist.append(a)
                    tufalist.append(i["formatted_answer"])
        if len(tulist)>0:
            tus=list(zip(tulist,tufalist,tualist))
            random.shuffle(tus)
            tulist,tufalist,tualist=zip(*tus)
    if tuorbon==1 or tuorbon==2:
        for i in data["data"]["bonuses"]:
            if len(i["texts"])!=0 and len(i["answers"])!=0 and i["tournament_id"]:
                if (i["category_id"] in clist or i["subcategory_id"] in sclist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist):
                    b=i["texts"]
                    b[0]=i["leadin"]+"\n"+b[0]
                    bonlist.append(b)
                    a=i["answers"]
                    for n,j in enumerate(a):
                        if j.find("&lt")>=0:
                            a[n]=j[:j.find("&lt")]
                        elif j.find("<")>=0:
                            a[n]=j[:j.find("<")]
                    bonalist.append(a)
                    bonfalist.append(i["formatted_answers"])
        if len(bonlist)>0:
            bons=list(zip(bonlist,bonfalist,bonalist))
            random.shuffle(bons)
            bonlist,bonfalist,bonalist=zip(*bons)
settourlist()
setup()
if (cc,sscc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None,None):
    if ttbb<2:
        tbrn=ttbb
    else:
        tbrn=0
    fetchqs(cc,sscc,dd,ttoouurr,ttbb)
    qscreen(ttbb,tthhyymmee)