import sys, tkinter as tk,enchant,random,json,datetime
from tkinter import messagebox
ccccc=["History/Life","Language","Literature","Mythology"]
ddddd=list(range(1,4))
diffdict={1:"Novice - Latin I",2:"Intermediate - Latin II",3:"Advanced - Latin III+"}
tttttooooouuuuurrrrr,tourids=dict(),dict()
cc,dd,ttoouurr,ttbb,tthhyymmee,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,root,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct,timeoutctr,endctr,qctr,qframe,data,curq,read=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
buzzed,reading,dead,ansalrgiven,qskipped,qfromreader=False,False,True,False,False,False
ptn,bagels=[0,0],[0,0,0]
tu,bon,tupts,bpts,tunum,bonnum,subbonnum,curwd,curbpts,tbrn,qlen=0,0,0,0,-1,-1,-1,0,0,0,0
tulist,tualist,tustatus,tuwd,tuid,bonid,bonlist,bonalist,bonstatus,subbonstatus,tutourlist,bontourlist,elerity,celerity,ielerity=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
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
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,background="#ffffff", relief=tk.SOLID, borderwidth=1,font=("segoe", "8", "normal"))
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
    global tourids,tttttooooouuuuurrrrr,data
    with open('certdict.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in ddddd:
        tttttooooouuuuurrrrr["Difficulty Level %s"%i]=set()
    for i in data["data"]["questions"]:
        if i["tournament_id"]:
            if i["tournament"]["name"] not in tourids:
                tourids[i["tournament"]["name"]]=(i["tournament_id"],i["tournament"]["year"])
            if "Difficulty Level %s"%i["tournament"]["difficulty_num"] in tttttooooouuuuurrrrr:
                tttttooooouuuuurrrrr["Difficulty Level %s"%i["tournament"]["difficulty_num"]].add(i["tournament"]["name"])
            else:
                tttttooooouuuuurrrrr["Difficulty Level %s"%i["tournament"]["difficulty_num"]]={i["tournament"]["name"]}
    for i in tttttooooouuuuurrrrr.keys():
        dddddddddd=dict()
        for j in tttttooooouuuuurrrrr[i]:
            if tourids[j][1] in dddddddddd:
                dddddddddd[tourids[j][1]].append(j)
            else:
                dddddddddd[tourids[j][1]]=[j]
        llllllllll=list()
        for j in sorted(dddddddddd.keys(),reverse=True):
            llllllllll.extend(sorted(dddddddddd[j]))
        tttttooooouuuuurrrrr[i]=llllllllll
def handback(c,d,tour,tb,tint):
    global cc,dd,ttoouurr,ttbb,tthhyymmee
    cc,dd,ttoouurr,ttbb,tthhyymmee=c,d,tour,tb,tint
    return
def gencard():
    s=''
    if len(tulist)!=0 or len(tulist)!=tustatus.count('skipped'):
        tstr='STATS\n'
        tstr+="\nTOSSUPS: %s"%len(tulist)
        tstr+="\nTOSSUPS SKIPPED: %s"%tustatus.count('skipped')
        tstr+="\nTOSSUPS HEARD: %s"%(tu)
        tstr+="\nTOSSUP POINTS: %s"%(tupts)
        tstr+="\nPOINTS PER TOSSUP HEARD: %s"%(0.0 if tu==0 else round(tupts/tu,2))
        tstr+="\nCORRECT/INCORRECT: %s/%s"%tuple(ptn)
        tstr+="\nAVERAGE QUESTION CELERITY: %s"%(sum(elerity)/len(elerity) if len(elerity)>0 else None)
        tstr+="\nAVERAGE CORRECT CELERITY: %s"%(sum(celerity)/len(celerity) if len(celerity)>0 else None)
        tstr+="\nAVERAGE INCORRECT CELERITY: %s"%(sum(ielerity)/len(ielerity) if len(ielerity)>0 else None)
        tstr+="\n"
        if len(bonlist)!=0:
            tstr+="\nBONUSES: %s"%len(bonlist)
            tstr+="\nBONUSES SKIPPED: %s"%bonstatus.count('skipped')
            tstr+="\nBONUSES HEARD: %s"%(bon)
            tstr+="\nBONUS POINTS: %s"%(bpts)
            tstr+="\nPOINTS PER BONUS HEARD: %s"%(0.0 if bon==0 else round(bpts/bon,2))
            tstr+="\n10s/5s/0s: %s/%s/%s\n"%tuple(bagels)
        ccc=0
        iii=0
        for i in range(len(tulist)):
            bz=False
            tstr+="\nTOSSUP #%s"%(i+1)
            if tustatus[i]!='skipped':
                wlist=tulist[i].split()
                if tuwd[i]!=-1:
                    bz=True
                    wlist[tuwd[i]-1]+=" 🔔"
                    if tustatus[i]>0:
                        ccc+=1
                    else:
                        iii+=1
                tstr+="\nTOURNAMENT: %s"%tutourlist[i][0]
                tstr+="\nDIFFICULTY: %s (%s)"%(tutourlist[i][1],diffdict[tutourlist[i][1]])
                tstr+="\nQUESTION: %s"%' '.join(wlist)
                tstr+="\nANSWER: %s"%tualist[i]
                tstr+="\nSCORE: %s"%(tustatus[i])
                if bz:
                    tstr+="\nCELERITY: %s"%elerity[ccc+iii-1]
                if tuid[i] in bonid:
                    tstr+='\nBONUS:'
                    ind=bonid.index(tuid[i])
                    if bonstatus[ind]!='skipped':
                        for j in range(len(bonlist[ind])):
                            tstr+="\nQUESTION: %s"%bonlist[ind][j]
                            tstr+="\nANSWER: %s"%bonalist[ind][j]
                            tstr+="\nSCORE: %s"%bonstatus[ind][j]
                    else:
                        tstr+='\n[skipped]'
            else:
                tstr+='\n[skipped]'
            tstr+="\n"
        s+=tstr
    if len(tulist)!=0 or len(bonlist)!=0:
        t=datetime.datetime.now()
        d=str(t.year)
        for i in (t.month, t.day, t.hour, t.minute, t.second):
            if len(str(i))<2:
                d+="0"
            d+=str(i)
        with open("stats-%s.txt"%d,'w',encoding='utf-8') as f:
            f.write(s)
def leavehomescreen():
    global cc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tualist,bonalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum
    if messagebox.askyesno("Leave?", "Do you want to quit this reader? (Press y/n)"):
        gencard()
        sys.exit()
def leavereader():
    global cc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tualist,bonalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum,tuwd,tutourlist,bontourlist,tuid,bonid
    if messagebox.askyesno("Leave?", "Do you want to quit this reader? (Press y/n)"):
        tuid=tuid[:tunum+1]
        bonid=bonid[:bonnum+1]
        tulist=tulist[:tunum+1]
        tualist=tualist[:tunum+1]
        tutourlist=tutourlist[:tunum+1]
        bonlist=bonlist[:bonnum+1]
        bonalist=bonalist[:bonnum+1]
        bontourlist=bontourlist[:bonnum+1]
        if reading or not (dead or ansalrgiven):
            if tbrn==0:
                tustatus.append('skipped')
                tuwd.append(-1)
            else:
                bonstatus.append('skipped')
                subbonstatus=[]
        gencard()
        sys.exit()
def setup():
    global qfromreader
    qfromreader=False
    root=tk.Tk()
    root.geometry("+20+20")
    root.focus_force()
    root.title("Certamen Reader of All Purposes")
    root.resizable(False,False)
    root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
    fram1=tk.Frame(root)
    fram1.grid(row=0,column=0)
    cats=[tk.IntVar() for i in range(len(ccccc))]
    catl=tk.Label(fram1, text = 'Categories: ', font=('calibri',10, 'bold'))
    catt=tk.Menubutton (fram1, text="Click to select options", relief=tk.RAISED)
    catt.menu =  tk.Menu (catt, tearoff = 0 )
    catt["menu"] = catt.menu
    for i in range(len(ccccc)):
        catt.menu.add_checkbutton(label=ccccc[i],variable=cats[i])
    if cc!=ccccc and cc:
        for i in cc:
            cats[ccccc.index(i)].set(1)
    lcats=tk.Button(fram1, text='❔')
    diffs=[tk.IntVar() for i in range(len(ddddd))]
    diffl=tk.Label(fram1, text = 'Difficulties: ', font=('calibri',10, 'bold'))
    difft=tk.Menubutton (fram1, text="Click to select options", relief=tk.RAISED)
    difft.menu =  tk.Menu (difft, tearoff = 0 )
    difft["menu"] = difft.menu
    for i in ddddd:
        difft.menu.add_checkbutton(label=i,variable=diffs[i-1])
    if dd!=ddddd and dd:
        for i in dd:
            diffs[i-1].set(1)
    ldiffs=tk.Button(fram1, text='❔')
    alltourlist=[]
    for i in tttttooooouuuuurrrrr:
        alltourlist.extend(tttttooooouuuuurrrrr[i])
    tours=[tk.IntVar() for i in range(len(alltourlist))]
    tourl=tk.Label(fram1, text = 'Tournaments: ', font=('calibri',10, 'bold'))
    tourt=tk.Menubutton (fram1, text="Click to select options", relief=tk.RAISED)
    tourt.menu =  tk.Menu (tourt, tearoff = 0 )
    tourt["menu"] = tourt.menu
    for n,i in enumerate(sorted(tttttooooouuuuurrrrr.keys())):
        tourt.menu.add_command(label=i,state='disabled')
        for j in tttttooooouuuuurrrrr[i]:
            tourt.menu.add_checkbutton(label=j,variable=tours[alltourlist.index(j)])
    if ttoouurr:
        for i in ttoouurr:
            tours[alltourlist.index(i)].set(1)
    ltours=tk.Button(fram1, text='❔')
    catl.grid(row=0,column=0, sticky="e")
    catt.grid(row=0,column=1,padx=(0,5))
    lcats.grid(row=0,column=2, sticky="w")
    CreateToolTip(lcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of categories: \n★ History/Life\n★ Language\n★ Literature\n★ Mythology\n\nEx. \n"Literature" → only gives questions from literature\n"History/Life, Mythology" → gives questions from history/life and mythology\n"Geography", "1" in difficulties → any questions on language of novice difficulty')
    diffl.grid(row=1,column=0, sticky="e")
    difft.grid(row=1,column=1,padx=(0,5))
    ldiffs.grid(row=1,column=2, sticky="w")
    CreateToolTip(ldiffs, text = 'Pick whatever difficulty levels you want via the dropdown menu. Leave blank for all. \nBelow is a list of all the difficulty level numbers and the difficulties they correspond to: \n★ 1 → Novice  - Latin I\n★ 2 → Intermediate  - Latin II\n★ 3 → Advanced  - Latin III+\n\nEx. \n"1" → questions with novice difficulty\n"1, 2, 3" → questions with difficulty ranging from hard novice to advanced\n"3", "2021 Yale Novice" in tournaments → any questions of advanced difficulty\n along with questions from 2021 Yale Novice packet')
    tourl.grid(row=2,column=0, sticky="e")
    tourt.grid(row=2,column=1,padx=(0,5))
    ltours.grid(row=2,column=2, sticky="w")
    CreateToolTip(ltours, text = 'Pick whatever tournaments you want via the dropdown menu. Leave blank for all. \n\nEx. \n"2021 Yale Intermediate" → 2021 Yale Intermediate packet, along with whatever \ndifficulty levels you have selected\n"2021 Yale Intermediate, 2021 Yale Advanced", selected "1" in difficulty levels → 2021 Yale Intermediate and \n2021 Yale Advanced, along with any questions of novice difficulty')
    fram2=tk.Frame(root)
    fram2.grid(row=1,column=0)
    timeo=tk.Label(fram2, text = 'Time between each word (ms): ', font=('calibri',10, 'bold'))
    times=tk.IntVar()
    timenter=tk.Entry(fram2,width=3,textvariable=times,)
    thyme = tk.Scale(fram2, from_=0, to=500, orient=tk.HORIZONTAL, length=400, tickinterval=50, variable=times)
    if type(tthhyymmee)==int:
        thyme.set(tthhyymmee)
    else:    
        thyme.set(250)
    timeex=tk.Button(fram2, text='❔')
    timeo.grid(row=0,column=0, sticky="e")
    timenter.grid(row=0,column=1)
    thyme.grid(row=0,column=2, sticky="w")
    timeex.grid(row=0,column=3, sticky="w")
    CreateToolTip(timeex, text = 'Changes interval between words. Higher values mean longer intervals and thus \nthe question is read slower. Smaller values mean shorter intervals and thus \nthe words are read faster. ')
    fram3=tk.Frame(root)
    fram3.grid(row=2,column=0)
    tubon=tk.IntVar()
    if ttbb:
        tubon.set(ttbb)
    tuorbon=tk.Label(fram3, text = 'What kind of questions do you want? ', font=('calibri',10, 'bold'))
    tu=tk.Radiobutton(fram3, text='Tossups only', variable=tubon, value=0)
    tunbon=tk.Radiobutton(fram3, text='Tossups and bonuses', variable=tubon, value=1)
    tubonex=tk.Button(fram3, text='❔')
    def submit():
        c=[ccccc[i] for i in range(len(ccccc)) if cats[i].get()>0]
        if c==[]:
            c=ccccc
        d=[ddddd[i] for i in range(len(ddddd)) if diffs[i].get()>0]
        t=[alltourlist[i] for i in range(len(alltourlist)) if tours[i].get()>0]
        if d==[] and t==[]:
            d=ddddd
        tb=tubon.get()
        tint=thyme.get()
        handback(c,d,t,tb,tint)
        root.destroy()
    fram4=tk.Frame(root)
    fram4.grid(row=3,column=0)
    abt=tk.Button(fram4,text = 'About')
    CreateToolTip(abt, text = "Hello, I'm GlutenFreeGrapes. I created this program in April 2022 \nas an all-in-one self-study certamen tool. \n\n★★★★★Why this?★★★★★\nI made this because despite the fact that there are numerous packets\nonline, there are no question databases to store them and no\nreaders to read from them. So, I decided to try and make one myself. \n\n★★★★★Credits★★★★★\nThis was inspired by my quizbowl question reader, QBits. \n\n★★★★★Contact★★★★★\nMy Github is @GlutenFreeGrapes. ")
    contr=tk.Button(fram4,text = 'Controls')
    sumbit=tk.Button(fram4,text = 'Go [Enter]', command = submit)
    CreateToolTip(contr, text = """Keybinds:\n[\] → [Next/Skip]\n[Space] → [Buzz]\n[Enter] → [Enter]\n[Escape] → [Back]\n[Ctrl+W] → [Leave]\n\nWhen the question starts, you will be able to live-adjust the time interval between words. \nDuring bonuses, the buzzer button should be disabled to prevent accidental buzzing during \nthem. You should be able to see your stats at the top of the window. """)
    quibt=tk.Button(fram4,text = 'Quit [Esc/Ctrl+W]', command = leavehomescreen)
    root.bind('<Return>',lambda event:submit())
    root.bind('<Escape>',lambda event:leavehomescreen())
    root.bind('<Control-w>',lambda event:leavehomescreen())
    tuorbon.grid(row=0,column=0, sticky="e")
    tu.grid(row=0,column=1, sticky="w")
    tunbon.grid(row=0,column=2, sticky="w")
    tubonex.grid(row=0,column=3, sticky="w")
    CreateToolTip(tubonex, text = 'Either practice on tossups only or do a normal packet reading')
    abt.grid(row=0,column=0,padx=(0,10),pady=(0,5))
    contr.grid(row=0,column=1,padx=(10,10),pady=(0,5))
    sumbit.grid(row=0,column=2,padx=(10,10),pady=(0,5))
    quibt.grid(row=0,column=3,padx=(10,0),pady=(0,5))
    root.mainloop()
def backtohomescreen():
    global cc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tualist,bonalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum,tuwd,tutourlist,bontourlist,tuid,bonid
    tuid=tuid[:tunum+1]
    bonid=bonid[:bonnum+1]
    tulist=tulist[:tunum+1]
    tualist=tualist[:tunum+1]
    tutourlist=tutourlist[:tunum+1]
    bonlist=bonlist[:bonnum+1]
    bonalist=bonalist[:bonnum+1]
    bontourlist=bontourlist[:bonnum+1]
    if reading or (not reading and not dead and not ansalrgiven):
        if tbrn==0:
            tustatus.append('skipped')
            tuwd.append(-1)
        else:
            bonstatus.append('skipped')
            subbonstatus=[]
    elif tbrn==1 and 0<len(subbonstatus)<3:
        bonstatus.append('skipped')
        subbonstatus=[]
    if qctr:
        qframe.after_cancel(qctr)
    if endctr:
        qframe.after_cancel(endctr)
    if timeoutctr:
        root.after_cancel(timeoutctr)
    root.destroy()
    buzzed,reading,dead,ansalrgiven,qskipped=False,False,True,False,False
    curwd,curbpts=0,0
    if tbrn==1:
        bonnum+=1
    subbonnum=-1
    setup()
    if (cc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None):
        tbrn=0
        fetchqs(cc,dd,ttoouurr,ttbb)
        qscreen(ttbb,tthhyymmee)
def qscreen(tuorbon,timeint):
    global buzzed,root,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct,qframe,tustatus,subbonstatus,bonstatus,qfromreader,read
    qfromreader=True
    root=tk.Tk()
    root.geometry("+20+20")
    root.title('Certamen Reader of All Purposes')
    root.resizable(False,False)
    root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
    topf=tk.Frame(root)
    topf.grid(row=0,column=0)
    statframe=tk.LabelFrame(topf, text='Stats')
    statframe.grid(row=0,column=0)
    pstatframe=tk.Frame(statframe)
    pstatframe.grid(row=0,column=0)
    cstatframe=tk.Frame(statframe)
    cstatframe.grid(row=1,column=0)
    tstatframe=tk.Frame(statframe)
    tstatframe.grid(row=2,column=0)
    qframe=tk.Frame(root)
    qframe.grid(row=1,column=0)
    qcanvas=tk.Canvas(qframe,width=650,height=450,background="white")
    qcanvas.pack()
    qtext=qcanvas.create_text(int(qcanvas['width'])/2,int(qcanvas['height'])/2,text='Press [Next/Skip] to start', width=qcanvas['width'], fill="black",font=("calibri",13))
    bframe=tk.LabelFrame(root, text='Controls')
    bframe.grid(row=2,column=0)
    controlframe=tk.Frame(bframe)
    controlframe.grid(row=0,column=0)
    qbt=tk.Button(topf,text='Back [Esc]',command=backtohomescreen)
    lbt=tk.Button(topf,text='Leave [Ctrl+W]',command=leavereader)
    buzzed=False
    tuct=tk.Label(pstatframe,text='Tossups: %s'%(tu))
    tossuppts=tk.Label(pstatframe,text='Tossup Points: %s'%(tupts))
    ppg=tk.Label(pstatframe,text='PPTUH: %s'%(0.0 if tu==0 else round(tupts/tu,2)))
    ptnct=tk.Label(pstatframe,text='Correct/Incorrect: %s'%('/'.join(str(i) for i in ptn)))
    bonct=tk.Label(pstatframe,text='Bonuses: %s'%(bon))
    bonuspts=tk.Label(pstatframe,text='Bonus Points: %s'%(bpts))
    ppb=tk.Label(pstatframe,text='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2)))
    tttb=tk.Label(pstatframe,text='10s/5s/0s: %s'%('/'.join(str(i) for i in bagels)))
    eler=tk.Label(cstatframe,text='Average Celerity: %s'%(round(sum(elerity)/len(elerity),3) if len(elerity)>0 else None))
    celer=tk.Label(cstatframe,text='Average Correct Celerity: %s'%(round(sum(celerity)/len(celerity),3) if len(celerity)>0 else None))
    ieler=tk.Label(cstatframe,text='Average Incorrect Celerity: %s'%(round(sum(ielerity)/len(ielerity),3) if len(ielerity)>0 else None))
    tourney=tk.Label(tstatframe,text='Tournament: ---')
    difficul=tk.Label(tstatframe,text='Difficulty: - (---)')
    is_this_correct=tk.StringVar()
    def buzzin():
        global buzzed,timeoutctr,root,enterans,elerity,read
        qcanvas.itemconfigure(qtext,text=' '.join(curq[:curwd+1])+' 🔔')
        elerity.append(max(1-(curwd+1)/qlen,0.0))
        root.unbind("<space>")        
        buzzed=True
        answerline['state']='normal'
        enterans['state']='normal'
        root.bind("<Return>", lambda event: checkanswer())
        buzzer['state']='disabled'
        root.unbind("<space>")
        read['state']='disabled'
        root.unbind('<\>')
        if endctr:
            qframe.after_cancel(endctr)
        answerline.focus_set()
        timeoutctr=root.after(10000,checkanswer)
    def checkanswer():
        global tu,tupts,bon,bpts,ptn,bagels,ansalrgiven,timeoutctr,reading,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,curbpts,tbrn,tustatus,bonstatus,subbonstatus,tuwd,elerity,celerity,ielerity,bonnum,read
        if not ansalrgiven and not dead:
            root.unbind("<Return>")
            if timeoutctr:
                root.after_cancel(timeoutctr)
            if endctr:
                qframe.after_cancel(endctr)
            givenans=is_this_correct.get()
            ansalrgiven=True
            answerline.delete(0,len(givenans))
            if tbrn==0:
                actualans=tualist[tunum]
                if buzzed:
                    if close_enough(givenans.lower(),actualans.lower()):
                        tupts+=10
                        ptn[0]+=1
                        tustatus.append(10)
                        celerity.append(elerity[-1])
                        if tuorbon==1:
                            tbrn=1
                    else:
                        if reading:
                            if prompt(givenans,actualans):
                                tupts+=10
                                ptn[0]+=1
                                tustatus.append(10)
                                celerity.append(elerity[-1])
                                if tuorbon==1:
                                    tbrn=1
                            else:
                                tupts-=0
                                ptn[1]+=1
                                tustatus.append(0)
                                ielerity.append(elerity[-1])
                                if tuorbon==1:
                                    bonstatus.append('skipped')
                        else:
                            if prompt(givenans,actualans):
                                tupts+=10
                                ptn[0]+=1
                                tustatus.append(10)
                                celerity.append(elerity[-1])
                                if tuorbon==1:
                                    tbrn=1
                            else:
                                tupts-=0
                                tustatus.append(0)
                                ielerity.append(elerity[-1])
                                if tuorbon==1:
                                    bonstatus.append('skipped')
                    tu+=1
                    tuwd.append(curwd)
                    qcanvas.itemconfigure(qtext,text=' '.join(curq[:curwd])+' 🔔 '+' '.join(curq[curwd:])+'\n\n'+tualist[tunum])
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    read['state']='normal'
                    root.bind('<\>', lambda event: readq())
                    reading=False
                    tuct['text']='Tossups: %s'%(tu)
                    tossuppts['text']='Tossup Points: %s'%(tupts)
                    ppg['text']='PPTUH: %s'%(0.0 if tu==0 else round(tupts/tu,2))
                    ptnct['text']='Correct/Incorrect: %s'%('/'.join(str(i) for i in ptn))
                    eler['text']='Average Celerity: %s'%(round(sum(elerity)/len(elerity),3) if len(elerity)>0 else None)
                    celer['text']='Average Correct Celerity: %s'%(round(sum(celerity)/len(celerity),3) if len(celerity)>0 else None)
                    ieler['text']='Average Incorrect Celerity: %s'%(round(sum(ielerity)/len(ielerity),3) if len(ielerity)>0 else None)
                    root.update()
            else:
                answerline['state']='disabled'
                enterans['state']='disabled'
                root.unbind("<Return>")
                actualans=bonalist[bonnum][subbonnum]
                if close_enough(givenans.lower(),actualans.lower()):
                    curbpts+=5
                    subbonstatus.append(5)
                else:
                    if prompt(givenans,actualans):
                        curbpts+=5
                        subbonstatus.append(5)
                    else:
                        curbpts+=0
                        subbonstatus.append(0)
                reading=False
                aread=bonlist[bonnum][:subbonnum]
                pretuwds=tulist[tunum].split()
                allread=' '.join(pretuwds[:tuwd[tunum]])+' 🔔 '+' '.join(pretuwds[tuwd[tunum]:])+'\n\n'+tualist[tunum]+'\n\n'
                for n,i in enumerate(aread):
                    allread+=i
                    allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
                qcanvas.itemconfigure(qtext,text=allread+bonlist[bonnum][subbonnum]+"\n\n"+bonalist[bonnum][subbonnum])
                read['state']='normal'
                root.bind('<\>', lambda event: readq())
                if subbonnum==len(bonlist[bonnum])-1:
                    bonstatus.append(subbonstatus)
                    subbonstatus=[]
                    bon+=1
                    bpts+=curbpts
                    bagels[(10-curbpts)//5]+=1
                    bonct['text']='Bonuses: %s'%(bon)
                    bonuspts['text']='Bonus Points: %s'%(bpts)
                    ppb['text']='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2))
                    tttb['text']='10s/5s/0s: %s'%('/'.join(str(i) for i in bagels))
                    root.update()
                    if tuorbon==1:
                        tbrn=1-tbrn
    answerline=tk.Entry(controlframe, textvariable = is_this_correct, width=30,state='disabled')
    enterans=tk.Button(controlframe,text="Enter [Enter]",command=checkanswer,state='disabled')
    enterans.grid(row=0,column=4)
    buzzer=tk.Button(controlframe,text="Buzz [space]",command=buzzin)
    if reading==False:
        buzzer['state']='disabled'
        root.unbind("<space>")
    tcframe=tk.Frame(bframe)
    tcframe.grid(row=2,column=0)
    timeo=tk.Label(tcframe, text = 'Time between each word (ms): ', font=('calibri',10, 'bold'))
    times=tk.IntVar()
    timenter=tk.Entry(tcframe,width=3,textvariable=times)
    thyme = tk.Scale(tcframe, from_=0, to=500, orient=tk.HORIZONTAL, length=400, tickinterval=50,variable=times)
    thyme.set(timeint)
    timeo.grid(row=0,column=0)
    timenter.grid(row=0,column=1)
    thyme.grid(row=0,column=2)
    def readq():
        global reading,buzzed,tunum,dead,ansalrgiven,qskipped,bonnum,subbonnum,curbpts,tustatus,bonstatus,subbonstatus,tuwd,read
        if dead or ansalrgiven:
            reading=True
            buzzed=False
            dead=False
            ansalrgiven=False
            qskipped=False
            if tuorbon==0 or (tuorbon==1 and tbrn==0):
                tunum+=1
            else:
                if subbonnum==len(bonlist[bonnum])-1 or bonnum<0:
                    bonnum+=1
                    subbonnum=0
                    curbpts=0
                else:
                    subbonnum+=1
            if tuorbon==0:
                if tunum>=len(tulist):
                    tunum-=1
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                    reading=False
                    dead=True
                    read['state']='disabled'
                    root.unbind('<\>')
                    thyme['state']='disabled'
                    timenter['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                if reading and tbrn==0:
                    buzzer['state']='normal'
                    root.bind("<space>", lambda event: buzzin())
                qcanvas.itemconfigure(qtext, font=("calibri",13))
                tourney['text']="Tournament: %s"%tutourlist[tunum][0]
                difficul['text']="Difficulty: %s (%s)"%(tutourlist[tunum][1],diffdict[tutourlist[tunum][1]])
                read_tossup(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    if tunum>=len(tulist):
                        tunum-=1
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                        reading=False
                        dead=True
                        read['state']='disabled'
                        root.unbind('<\>')
                        thyme['state']='disabled'
                        timenter['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    if reading and tbrn==0:
                        buzzer['state']='normal'
                        root.bind("<space>", lambda event: buzzin())
                    qcanvas.itemconfigure(qtext, font=("calibri",13))
                    tourney['text']="Tournament: %s"%tutourlist[tunum][0]
                    difficul['text']="Difficulty: %s (%s)"%(tutourlist[tunum][1],diffdict[tutourlist[tunum][1]])
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    if bonnum>=len(bonlist):
                        bonnum-=1
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                        reading=False
                        dead=True
                        read['state']='disabled'
                        root.unbind('<\>')
                        thyme['state']='disabled'
                        timenter['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    if reading and tbrn==1:
                        read['state']='disabled'
                        root.unbind('<\>')
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='normal'
                        enterans['state']='normal'
                        root.bind("<Return>", lambda event: checkanswer())
                    qcanvas.itemconfigure(qtext, font=("calibri",13))
                    answerline.focus_set()
                    tourney['text']="Tournament: %s"%bontourlist[bonnum][0]
                    difficul['text']="Difficulty: %s (%s)"%(bontourlist[bonnum][1],diffdict[bontourlist[bonnum][1]])
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
                tuwd.append(-1)
                tustatus.append('skipped')
                tunum+=1
                if tunum>=len(tulist):
                    tunum-=1
                    qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                    reading=False
                    dead=True
                    read['state']='disabled'
                    root.unbind('<\>')
                    thyme['state']='disabled'
                    timenter['state']='disabled'
                    buzzer['state']='disabled'
                    root.unbind("<space>")
                    answerline['state']='disabled'
                    enterans['state']='disabled'
                    root.unbind("<Return>")
                    return
                qcanvas.itemconfigure(qtext, font=("calibri",13))
                tourney['text']="Tournament: %s"%tutourlist[tunum][0]
                difficul['text']="Difficulty: %s (%s)"%(tutourlist[tunum][1],diffdict[tutourlist[tunum][1]])
                read_tossup(qframe,qcanvas,qtext,thyme)
            else:
                if tbrn==0:
                    tuwd.append(-1)
                    tustatus.append('skipped')
                    tunum+=1
                    if tunum>=len(tulist):
                        tunum-=1
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                        reading=False
                        dead=True
                        read['state']='disabled'
                        root.unbind('<\>')
                        thyme['state']='disabled'
                        timenter['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    qcanvas.itemconfigure(qtext, font=("calibri",13))
                    tourney['text']="Tournament: %s"%tutourlist[tunum][0]
                    difficul['text']="Difficulty: %s (%s)"%(tutourlist[tunum][1],diffdict[tutourlist[tunum][1]])
                    read_tossup(qframe,qcanvas,qtext,thyme)
                else:
                    bonstatus.append('skipped')
                    subbonstatus=[]
                    bonnum+=1
                    subbonnum=0
                    curbpts=0
                    if bonnum>=len(bonlist):
                        bonnum-=1
                        qcanvas.itemconfigure(qtext, text = "No more questions left 😔\nPress [Back] to get new questions\nPress [Leave] to exit")
                        reading=False
                        dead=True
                        read['state']='disabled'
                        root.unbind('<\>')
                        thyme['state']='disabled'
                        timenter['state']='disabled'
                        buzzer['state']='disabled'
                        root.unbind("<space>")
                        answerline['state']='disabled'
                        enterans['state']='disabled'
                        root.unbind("<Return>")
                        return
                    qcanvas.itemconfigure(qtext, font=("calibri",13))
                    answerline.focus_set()
                    tourney['text']="Tournament: %s"%bontourlist[bonnum][0]
                    difficul['text']="Difficulty: %s (%s)"%(bontourlist[bonnum][1],diffdict[bontourlist[bonnum][1]])
                    read_bonus(qframe,qcanvas,qtext,thyme)
    read=tk.Button(controlframe,text="Next/Skip [\]",command=readq)
    root.bind('<\>', lambda event: readq())
    read.grid(row=0,column=0)
    eler.grid(row=0,column=0)
    celer.grid(row=0,column=1)
    ieler.grid(row=0,column=2)
    tourney.grid(row=0,column=0)
    difficul.grid(row=0,column=1)
    if tuorbon==0:
        tuct.grid(row=0,column=0)
        tossuppts.grid(row=0,column=1)
        ppg.grid(row=0,column=2)
        ptnct.grid(row=0,column=3)
    else:
        tuct.grid(row=0,column=0)
        tossuppts.grid(row=0,column=1)
        ppg.grid(row=0,column=2)
        ptnct.grid(row=0,column=3)
        bonct.grid(row=1,column=0)
        bonuspts.grid(row=1,column=1)
        ppb.grid(row=1,column=2)
        tttb.grid(row=1,column=3)
    answerline.grid(row=0,column=3,padx=(5,5))
    buzzer.grid(row=0,column=2,padx=(5,5))
    qbt.grid(row=0,column=1,padx=(5,5))
    lbt.grid(row=0,column=2)
    root.bind('<Escape>',lambda event:backtohomescreen())
    root.bind('<Control-w>',lambda event:leavereader())
    root.focus_force()
    def close_enough(given,normalans):
        nans=normalans.replace('[accept equivalents]','')
        possans=set()
        n=nans.split('/')
        if n!=None:
            possans.update({i.strip() for i in n if i!=''})
        n=nans.split(' or ')
        if n!=None:
            possans.update({i.strip() for i in n if i!=''})
        possans.update({ignorparens(i).strip() for i in possans})
        for i in possans:
            if enchant.utils.levenshtein(given,i)<min(3,len(i)//2):
                return True
        if enchant.utils.levenshtein(given,normalans)<min(3,len(normalans)//2):
            return True
        return False
    def check_if_buzz_at_eotu():
        global dead,tu,tuct,tossuppts,ppg,ptnct,root,buzzer,qcanvas,qtext,reading,tuwd,tbrn
        if reading==False and buzzed==False:
            if ttbb==1:
                tbrn=0
            tuwd.append(-1)
            dead=True
            tustatus.append(0)
            tu+=1
            qcanvas.itemconfigure(qtext,text=tulist[tunum]+'\n\n'+tualist[tunum])
            tuct['text']='Tossups: %s'%(tu)
            ppg['text']='PPTUH: %s'%(0.0 if tu==0 else round(tupts/tu,2))
            buzzer['state']='disabled'
            root.unbind("<space>")
            root.update()
    def check_if_buzz_at_eobon():
        global dead,bon,bonct,bonuspts,ppb,tttb,curbpts,answerline,reading,tbrn,bagels,bpts,subbonstatus,bonstatus,read
        ans=is_this_correct.get()
        if ans!="":
            answerline.delete(0,len(ans))
            if close_enough(ans.lower(),bonalist[bonnum][subbonnum].lower()):
                curbpts+=5
                subbonstatus.append(5)
            else:
                if prompt(ans,bonalist[bonnum][subbonnum]):
                    curbpts+=5
                    subbonstatus.append(5)
                else:
                    curbpts+=0
                    subbonstatus.append(0)
        root.bind('<\>',lambda event: readq())
        if reading==False and ansalrgiven==False:
            dead=True
            subbonstatus.append(0)
            if ttbb==1 and subbonnum==len(bonlist[bonnum])-1:
                tbrn=0
            if subbonnum==len(bonlist[bonnum])-1:
                bonstatus.append(subbonstatus)
                subbonstatus=[]
                bon+=1
                bagels[(10-curbpts)//5]+=1
                bpts+=curbpts
                bonct['text']='Bonuses: %s'%(bon)
                bonuspts['text']='Bonus Points: %s'%(bpts)
                ppb['text']='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2))
                tttb['text']='10s/5s/0s: %s'%('/'.join(str(i) for i in bagels))
            answerline['state']='disabled'
            enterans['state']='disabled'
            root.unbind("<Return>")
            read['state']='normal'
            aread=bonlist[bonnum][:subbonnum]
            pretuwds=tulist[tunum].split()
            allread=' '.join(pretuwds[:tuwd[tunum]])+' 🔔 '+' '.join(pretuwds[tuwd[tunum]:])+'\n\n'+tualist[tunum]+'\n\n'
            for n,i in enumerate(aread):
                allread+=i
                allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
            qcanvas.itemconfigure(qtext,text=allread+bonlist[bonnum][subbonnum]+"\n\n"+bonalist[bonnum][subbonnum])
    def read_tossup(window,canvas,question_txt,timeint):
        global qlen,curq
        current_q = tulist[tunum]
        words=current_q.split()
        qlen=len(words)
        curq=words
        itertu(words, 1, window,canvas,question_txt,timeint)
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
        aread = current_q[:subbonnum]
        pretuwds=tulist[tunum].split()
        allread=' '.join(pretuwds[:tuwd[tunum]])+' 🔔 '+' '.join(pretuwds[tuwd[tunum]:])+'\n\n'+tualist[tunum]+'\n\n'
        for n,i in enumerate(aread):
            allread+=i
            allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
        iterbon(allread,bonwords, 1, window,canvas,question_txt,timeint)
    def iterbon(allread, words, i, window,canvas,question_txt,timeint):
        if i > len(words):
            global reading,endctr,qctr
            reading=False
            endctr=window.after(15000,check_if_buzz_at_eobon)
            return
        if qskipped:
            return
        if not ansalrgiven:
            canvas.itemconfigure(question_txt, text=allread+' '.join(words[:i]))
            i += 1
            qctr = window.after(timeint.get(), lambda: iterbon(allread,words, i,window,canvas,question_txt,timeint))
    root.mainloop()
def prompt(gans,aans):
        if gans.strip()=='idk' or gans.strip()=='' or (gans.strip()=="n" and aans!="n"):
            return False
        return messagebox.askyesno("Were you correct?","Were you correct? (Press y/n)\nYour answer: %s\nActual answer: %s"%(gans,aans))
def ignorparens(s):
    parenpairs=set()
    pp=set()
    lparen=[]
    for n,i in enumerate(s):
        if i=='(':
            lparen.append((i,n))
        elif i==')':
            parenpairs.add((lparen.pop()[1],n))
    for i in parenpairs:
        for j in parenpairs:
            if i!=j and i[0]<j[0] and j[1]<i[1]:
                pp.add(j)
    parts=sorted([i for i in parenpairs if i not in pp])
    if len(parts)>0:
        fstr=s[:parts[0][0]]
        for i in range(len(parts)-1):
            fstr+=s[parts[i][1]+1:parts[i+1][0]]
        fstr+=s[parts[-1][1]+1:]
    else:
        fstr=s
    return fstr
def stripemsub(s):
    s=s.replace("<em>","")
    s=s.replace("</em>","")
    s=s.replace("<sub>","")
    s=s.replace("</sub>","")
    return s
def fetchqs(cats,diffs,tours,tuorbon):
    global tulist,tualist,bonlist,bonalist,tutourlist,bontourlist,tuid,bonid
    catids={"Language":2,"History/Life":1,"Mythology":4,"Literature":3}
    t,ttt,tttt,bbb,bbbbb,bbbbbb,tid,bid=[],[],[],[],[],[],[],[]
    clist=set()
    dlist=set(diffs)
    tlist=set()
    for i in cats:
        clist.add(catids[i])
    for i in tours:
        tlist.add(tourids[i][0])
    if tuorbon==0:
        for i in data["data"]["questions"]:
            if i["text"]!="[missing]" and i["answer"]!="[missing]" and i["tournament_id"]:
                if ((i["category_id"] in clist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist)) and i["text"] not in tulist:
                    z=i["text"]
                    z=stripemsub(z)
                    t.append(z)
                    a=i["answer"]
                    a=stripemsub(a)
                    ttt.append(a)
                    tttt.append((i["tournament"]["name"],i["tournament"]["difficulty_num"]))
                    tid.append(i["id"])
        if len(t)>0:
            tus=list(zip(t,ttt,tttt,tid))
            random.shuffle(tus)
            t,ttt,tttt,tid=zip(*tus)
            tulist.extend(list(t))
            tualist.extend(list(ttt))
            tutourlist.extend(list(tttt))
            tuid.extend(tid)
    else:
        for i in data["data"]["questions"]:
            if i["text"]!="[missing]" and i["answer"]!="[missing]" and i["tournament_id"]:
                if ((i["category_id"] in clist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist)) and i["text"] not in tulist and len(i["texts"])>0:
                    z=i["text"]
                    z=stripemsub(z)
                    t.append(z)
                    a=i["answer"]
                    a=stripemsub(a)
                    ttt.append(a)
                    tttt.append((i["tournament"]["name"],i["tournament"]["difficulty_num"]))
                    tid.append(i["id"])
            if len(i["texts"])!=0 and len(i["answers"])!=0 and i["tournament_id"]:
                b=i["texts"]
                if((i["category_id"] in clist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist))and b not in bonlist and i["id"] not in tuid:
                    for n,j in enumerate(b):
                        b[n]=stripemsub(j)
                    bbb.append(b)
                    a=i["answers"]
                    for n,j in enumerate(a):
                        k=stripemsub(j)
                        a[n]=k
                    bbbbb.append(a)
                    bid.append(i["id"])
                    bbbbbb.append((i["tournament"]["name"],i["tournament"]["difficulty_num"]))
        if len(t)>0:
            tubons=list(zip(t,ttt,tttt,tid,bbb,bbbbb,bbbbbb,bid))
            random.shuffle(tubons)
            t,ttt,tttt,tid,bbb,bbbbb,bbbbbb,bid=zip(*tubons)
            tulist.extend(list(t))
            tualist.extend(list(ttt))
            tutourlist.extend(list(tttt))
            bonlist.extend(list(bbb))
            bonalist.extend(list(bbbbb))
            bontourlist.extend(list(bbbbbb))
            tuid.extend(tid)
            bonid.extend(bid)
settourlist()
setup()
if (cc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None):
    tbrn=0
    fetchqs(cc,dd,ttoouurr,ttbb)
    qscreen(ttbb,tthhyymmee)