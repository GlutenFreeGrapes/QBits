import sys, tkinter as tk,enchant,random,json,bs4,datetime
from tkinter import messagebox
ccccc=["Current Events", "Fine Arts", "Geography", "History", "Literature", "Mythology", "Philosophy", "Religion", "Science", "Social Science", "Trash"]
sssssccccc={"Current Events Subcategories":["American Current Events", "Other Current Events"], "Fine Arts Subcategories":["American Fine Arts", "Audiovisual Fine Arts", "Auditory Fine Arts", "British Fine Arts", "European Fine Arts", "Opera", "Visual Fine Arts", "World Fine Arts", "Other Fine Arts"], "Geography Subcategories":["American Geography", "World Geography"], "History Subcategories":["American History", "British History", "Classical History", "European History", "World History", "Other History"], "Literature Subcategories":["American Literature", "British Literature", "Classical Literature", "European Literature", "World Literature", "Other Literature"], "Mythology Subcategories":["American Mythology", "Chinese Mythology", "Egyptian Mythology", "Greco-Roman Mythology", "Indian Mythology", "Japanese Mythology", "Norse Mythology", "Other East Asian Mythology", "Other Mythology"], "Philosophy Subcategories":["American Philosophy", "Classical Philosophy", "East Asian Philosophy", "European Philosophy", "Other Philosophy"], "Religion Subcategories":["American Religion", "Christianity", "East Asian Religion", "Islam", "Judaism", "Other Religion"], "Science Subcategories":["American Science", "Biology", "Chemistry", "Computer Science", "Math", "Physics", "World Science", "Other Science"], "Social Science Subcategories":["American Social Science", "Anthropology", "Economics", "Linguistics", "Political Science", "Psychology", "Sociology", "Other Social Science"], "Trash Subcategories":["American Trash", "Movies", "Music", "Sports", "Television", "Video Games", "Other Trash"]}
ddddd=list(range(1,10))
diffdict={1:"Middle School",2:"Easy High School",3:"Regular High School",4:"Hard High School",5:"High School Nationals",6:"Easy College",7:"Regular College",8:"Hard College",9:"Open"}
tttttooooouuuuurrrrr,tourids=dict(),dict()
cc,sscc,dd,ttoouurr,ttbb,tthhyymmee,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,root,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct,timeoutctr,endctr,qctr,qframe,data,curq=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
buzzed,reading,dead,ansalrgiven,qskipped,qfromreader=False,False,True,False,False,False
ptn,bagels=[0,0,0],[0,0,0,0]
tu,bon,tupts,bpts,tunum,bonnum,subbonnum,pm,curwd,curbpts,tbrn,qlen=0,0,0,0,-1,-1,0,0,0,0,0,0
tulist,tualist,tufalist,tustatus,tuwd,bonlist,bonalist,bonfalist,bonstatus,subbonstatus,tutourlist,bontourlist,elerity,celerity,ielerity=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
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
    global tourids,tttttooooouuuuurrrrr,data
    with open('qdbcompressed.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in ddddd:
        tttttooooouuuuurrrrr["Difficulty Level %s"%i]=set()
    for j in data["data"]["tossups"],data["data"]["bonuses"]:
        for i in j:
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
def handback(c,sc,d,tour,tb,tint):
    global cc,sscc,dd,ttoouurr,ttbb,tthhyymmee
    cc,sscc,dd,ttoouurr,ttbb,tthhyymmee=c,sc,d,tour,tb,tint
    return
def gencard():
    s=''
    if len(tulist)!=0 or len(tulist)!=tustatus.count('skipped'):
        tstr='TOSSUPS\n'
        tstr+="\nTOSSUPS: %s"%len(tulist)
        tstr+="\nTOSSUPS SKIPPED: %s"%tustatus.count('skipped')
        tstr+="\nTOSSUPS HEARD: %s"%(tu)
        tstr+="\nTOSSUP POINTS: %s"%(tupts)
        tstr+="\nPOINTS PER TOSSUP HEARD: %s"%(0.0 if tu==0 else round(tupts/tu,2))
        tstr+="\n15s/10s/0s/-5s: %s/%s/%s/%s"%(ptn[0],ptn[1],tustatus.count(0),ptn[2])
        tstr+="\nAVERAGE QUESTION CELERITY: %s"%(sum(elerity)/len(elerity) if len(elerity)>0 else None)
        tstr+="\nAVERAGE CORRECT CELERITY: %s"%(sum(celerity)/len(celerity) if len(celerity)>0 else None)
        tstr+="\nAVERAGE INCORRECT CELERITY: %s"%(sum(ielerity)/len(ielerity) if len(ielerity)>0 else None)
        tstr+="\n"
        ccc=0
        iii=0
        for i in range(len(tulist)):
            bz=False
            tstr+="\nTOSSUP #%s"%(i+1)
            if tustatus[i]!='skipped':
                wlist=tulist[i].split()
                for k in range(len(wlist)):
                    j=wlist[k].find("(*)")
                    if j!=-1:
                        if wlist[k]=="(*)":
                            wlist.pop(k)
                            wlist[k-1]=wlist[k-1]+" (*)"
                            break
                        elif j==(len(wlist[k])-3):
                            wlist[k]=wlist[k].replace("(*)"," (*)")
                            break
                        elif j==0:
                            wlist[k]=wlist[k][3:]
                            wlist[k-1]=wlist[k-1]+" (*)"
                            break
                        elif j>=0:
                            n=wlist[k][j+3:]
                            wlist[k]=wlist[k][:j]+" (*)"
                            wlist.insert(k+1,n)
                            break
                if tuwd[i]!=-1:
                    bz=True
                    if wlist[tuwd[i]-1].find("(*)")<0:
                        wlist[tuwd[i]-1]+=" 🔔"
                    else:
                        wlist[tuwd[i]-1]=wlist[tuwd[i]-1][:len(wlist[tuwd[i]-1])-3]+" 🔔 (*)"
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
            else:
                tstr+='\n[skipped]'
            tstr+="\n"
        s+=tstr
    if len(tulist)!=0 and len(bonlist)!=0:
        s+="\n\n"
    if len(bonlist)!=0 or len(bonlist)!=bonstatus.count('skipped'):
        bstr='BONUSES\n'
        bstr+="\nBONUSES: %s"%len(bonlist)
        bstr+="\nBONUSES SKIPPED: %s"%bonstatus.count('skipped')
        bstr+="\nBONUSES HEARD: %s"%(bon)
        bstr+="\nBONUS POINTS: %s"%(bpts)
        bstr+="\nPOINTS PER BONUS HEARD: %s"%(0.0 if bon==0 else round(bpts/bon,2))
        bstr+="\n30s/20s/10s/0s: %s/%s/%s/%s"%tuple(bagels)
        bstr+="\n"
        for i in range(len(bonlist)):
            bstr+="\nBONUS #%s"%(i+1)
            if bonstatus[i]!='skipped':
                bstr+="\nTOURNAMENT: %s"%bontourlist[i][0]
                bstr+="\nDIFFICULTY: %s (%s)"%(bontourlist[i][1],diffdict[bontourlist[i][1]])
                for j in range(len(bonlist[i])):
                    bstr+="\nQUESTION: %s"%bonlist[i][j]
                    bstr+="\nANSWER: %s"%bonalist[i][j]
                    bstr+="\nSCORE: %s"%bonstatus[i][j]
            else:
                bstr+='\n[skipped]'
            bstr+="\n"
        s+=bstr
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
    global cc,sscc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tufalist,tualist,bonalist,bonfalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,pm,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum
    if messagebox.askyesno("Leave?", "Do you want to quit this reader? (Press y/n)"):
        gencard()
        sys.exit()
def leavereader():
    global cc,sscc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tufalist,tualist,bonalist,bonfalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,pm,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum,tuwd,tutourlist,bontourlist
    if messagebox.askyesno("Leave?", "Do you want to quit this reader? (Press y/n)"):
        tulist=tulist[:tunum+1]
        tualist=tualist[:tunum+1]
        tufalist=tufalist[:tunum+1]
        tutourlist=tutourlist[:tunum+1]
        bonlist=bonlist[:bonnum+1]
        bonalist=bonalist[:bonnum+1]
        bonfalist=bonfalist[:bonnum+1]
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
    root.title("QBits")
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
    allsubcatlist=[]
    for i in sssssccccc:
        allsubcatlist.extend(sssssccccc[i])
    subcats=[tk.IntVar() for i in range(len(allsubcatlist))]
    subcatl=tk.Label(fram1, text = 'Subcategories: ', font=('calibri',10, 'bold'))
    subcatt=tk.Menubutton (fram1, text="Click to select options", relief=tk.RAISED)
    subcatt.menu =  tk.Menu (subcatt, tearoff = 0 )
    subcatt["menu"] = subcatt.menu
    for n,i in enumerate(sorted(sssssccccc.keys())):
        subcatt.menu.add_command(label=i,state='disabled')
        for j in sssssccccc[i]:
            subcatt.menu.add_checkbutton(label=j,variable=subcats[allsubcatlist.index(j)])
    if sscc:
        for i in sscc:
            subcats[allsubcatlist.index(i)].set(1)
    lsubcats=tk.Button(fram1, text='❔')
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
    CreateToolTip(lcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of categories: \n★ Current Events\n★ Fine Arts\n★ Geography\n★ History\n★ Literature\n★ Mythology\n★ Philosophy\n★ Religion\n★ Science\n★ Social Science\n★ Trash\n\nEx. \n"Current Events" → only gives questions from current events\n"History, Mythology, Science" → gives questions from history, mythology, and science\n"Geography", "Video Games" in subcategories → any questions on geography, \nalong with video game questions')
    subcatl.grid(row=1,column=0, sticky="e")
    subcatt.grid(row=1,column=1,padx=(0,5))
    lsubcats.grid(row=1,column=2, sticky="w")
    CreateToolTip(lsubcats, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \nList of subcategories: \n\n★ Current Events Subcategories: American Current Events, Other Current Events\n★ Fine Arts Subcategories: American Fine Arts, Audiovisual Fine Arts, \nAuditory Fine Arts, British Fine Arts, European Fine Arts, Opera, Visual Fine Arts, \nWorld Fine Arts, Other Fine Arts\n★ Geography Subcategories: American Geography, World Geography\n★ History Subcategories: American History, British History, European History, \nClassical History, World History, Other History\n★ Literature Subcategories: American Literature, British Literature, \nEuropean Literature, Classical Literature, World Literature, Other Literature\n★ Mythology Subcategories: American Mythology, Chinese Mythology, Egyptian Mythology, \nGreco-Roman Mythology, Indian Mythology, Japanese Mythology, Norse Mythology, \nOther East Asian Mythology, Other Mythology\n★ Philosophy Subcategories: American Philosophy, Classical Philosophy, \nEast Asian Philosophy, European Philosophy, Other Philosophy\n★ Religion Subcategories: American Religion, Christianity, East Asian Religion, \nIslam, Judaism, Other Religion\n★ Science Subcategories: American Science, Biology, Chemistry, Computer Science, \nMath, Physics, World Science, Other Science\n★ Social Science Subcategories: American Social Science, Anthropology, Economics, \nLinguistics, Political Science, Psychology, Sociology, Other Social Science\n★ Trash Subcategories: American Trash, Movies, Music, Sports, Television, \nVideo Games, Other Trash\n\nEx. \n"Greco-Roman Mythology, Computer Science" → only gives greco-roman mythology and \ncomputer science questions\n"Physics", "Literature" in categories → any questions on physics, along with literature\n questions')
    diffl.grid(row=2,column=0, sticky="e")
    difft.grid(row=2,column=1,padx=(0,5))
    ldiffs.grid(row=2,column=2, sticky="w")
    CreateToolTip(ldiffs, text = 'Pick whatever question difficulty levels you want, separated by commas. Leave blank for all. \nBelow is a list of all the difficulty level numbers and the difficulties they correspond to: \n1 → Middle School\n2 → Easy High School\n3 → Regular High School\n4 → Hard High School\n5 → National High School\n6 → Easy College\n7 → Regular College\n8 → Hard College\n9 → Open\n\nEx. \n"6" → questions with easy college difficulty\n"4,5,6,7" → questions with difficulty ranging from hard high school to regular college\n"6", "2020 Oxford Online" in tournaments → any questions in difficulty level 6\n along with questions from 2020 Oxford Online packet')
    tourl.grid(row=3,column=0, sticky="e")
    tourt.grid(row=3,column=1,padx=(0,5))
    ltours.grid(row=3,column=2, sticky="w")
    CreateToolTip(ltours, text = 'Pick whatever categories you want via the dropdown menu. Leave blank for all. \n\nEx. \n"2020 CALISTO" → 2020 CALISTO packet, along with whatever \ndifficulty levels you have selected\n"2020 CALISTO, 2020 Terrapin", selected "6" in difficulty level → 2020 CALISTO and \n2020 Terrapin, along with any questions with diffuculty level 6')
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
    bon=tk.Radiobutton(fram3, text='Bonuses only', variable=tubon, value=1)
    tunbon=tk.Radiobutton(fram3, text='Tossups and bonuses', variable=tubon, value=2)
    tubonex=tk.Button(fram3, text='❔')
    def submit():
        c=[ccccc[i] for i in range(len(ccccc)) if cats[i].get()>0]
        sc=[allsubcatlist[i] for i in range(len(allsubcatlist)) if subcats[i].get()>0]
        if c==[] and sc==[]:
            c=ccccc
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
    sumbit=tk.Button(fram4,text = 'Go [Enter]', command = submit)
    CreateToolTip(contr, text = """Keybinds:\n[\] → [Next/Skip]\n[Space] → [Buzz]\n[Enter] → [Enter]\n[Escape] → [Back]\n[Ctrl+W] → [Leave]\n\nWhen the question starts, you will be able to live-adjust the time interval between words. \nDuring bonuses, the buzzer button should be disabled to prevent accidental buzzing during \nthem. You should be able to see your stats at the top of the window. """)
    quibt=tk.Button(fram4,text = 'Quit [Esc/Ctrl+W]', command = leavehomescreen)
    root.bind('<Return>',lambda event:submit())
    root.bind('<Escape>',lambda event:leavehomescreen())
    root.bind('<Control-w>',lambda event:leavehomescreen())
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
def backtohomescreen():
    global cc,sscc,dd,ttoouurr,ttbb,tthhyymmee,tbrn,root,tulist,bonlist,tufalist,tualist,bonalist,bonfalist,qframe,buzzed,reading,dead,ansalrgiven,qskipped,subbonnum,pm,curwd,curbpts,tustatus,bonstatus,subbonstatus,tunum,bonnum,tuwd,tutourlist,bontourlist
    tulist=tulist[:tunum+1]
    tualist=tualist[:tunum+1]
    tufalist=tufalist[:tunum+1]
    tutourlist=tutourlist[:tunum+1]
    bonlist=bonlist[:bonnum+1]
    bonalist=bonalist[:bonnum+1]
    bonfalist=bonfalist[:bonnum+1]
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
    pm,curwd,curbpts=0,0,0
    if tbrn==1:
        bonnum+=1
    subbonnum=-1
    setup()
    if (cc,sscc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None,None):
        if ttbb<2:
            tbrn=ttbb
        else:
            tbrn=0
        fetchqs(cc,sscc,dd,ttoouurr,ttbb)
        qscreen(ttbb,tthhyymmee)
def qscreen(tuorbon,timeint):
    global buzzed,root,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,buzzer,enterans,answerline,qcanvas,qtext,is_this_correct,qframe,tustatus,subbonstatus,bonstatus,qfromreader
    qfromreader=True
    root=tk.Tk()
    root.geometry("+20+20")
    root.title('QBits')
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
    ptnct=tk.Label(pstatframe,text='Powers/10s/Negs: %s'%('/'.join(str(i) for i in ptn)))
    bonct=tk.Label(pstatframe,text='Bonuses: %s'%(bon))
    bonuspts=tk.Label(pstatframe,text='Bonus Points: %s'%(bpts))
    ppb=tk.Label(pstatframe,text='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2)))
    tttb=tk.Label(pstatframe,text='30s/20s/10s/0s: %s'%('/'.join(str(i) for i in bagels)))
    eler=tk.Label(cstatframe,text='Average Celerity: %s'%(round(sum(elerity)/len(elerity),3) if len(elerity)>0 else None))
    celer=tk.Label(cstatframe,text='Average Correct Celerity: %s'%(round(sum(celerity)/len(celerity),3) if len(celerity)>0 else None))
    ieler=tk.Label(cstatframe,text='Average Incorrect Celerity: %s'%(round(sum(ielerity)/len(ielerity),3) if len(ielerity)>0 else None))
    tourney=tk.Label(tstatframe,text='Tournament: ---')
    difficul=tk.Label(tstatframe,text='Difficulty: - (---)')
    is_this_correct=tk.StringVar()
    def buzzin():
        global buzzed,timeoutctr,root,enterans,elerity
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
        timeoutctr=root.after(8000,checkanswer)
    def checkanswer():
        global tu,tupts,bon,bpts,ptn,bagels,ansalrgiven,timeoutctr,reading,tuct,tossuppts,ppg,ptnct,bonct,bonuspts,ppb,tttb,curbpts,tbrn,tustatus,bonstatus,subbonstatus,tuwd,elerity,celerity,ielerity
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
                fans=tufalist[tunum]
                actualans=tualist[tunum]
                if buzzed:
                    if close_enough(givenans.lower(),fans,actualans.lower()):
                        if curwd<=pm:
                            tupts+=15
                            ptn[0]+=1
                            tustatus.append(15)
                        else:
                            tupts+=10
                            ptn[1]+=1
                            tustatus.append(10)
                        celerity.append(elerity[-1])
                        if tuorbon==2:
                            tbrn=1
                    else:
                        if reading:
                            if prompt(givenans,actualans):
                                if curwd<=pm:
                                    tupts+=15
                                    ptn[0]+=1
                                    tustatus.append(15)
                                else:
                                    tupts+=10
                                    ptn[1]+=1
                                    tustatus.append(10)
                                celerity.append(elerity[-1])
                                if tuorbon==2:
                                    tbrn=1
                            else:
                                tupts-=5
                                ptn[2]+=1
                                tustatus.append(-5)
                                ielerity.append(elerity[-1])
                        else:
                            if prompt(givenans,actualans):
                                if curwd<=pm:
                                    tupts+=15
                                    ptn[0]+=1
                                    tustatus.append(15)
                                else:
                                    tupts+=10
                                    ptn[1]+=1
                                    tustatus.append(10)
                                celerity.append(elerity[-1])
                                if tuorbon==2:
                                    tbrn=1
                            else:
                                tupts-=0
                                tustatus.append(0)
                                ielerity.append(elerity[-1])
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
                    ptnct['text']='Powers/10s/Negs: %s'%('/'.join(str(i) for i in ptn))
                    eler['text']='Average Celerity: %s'%(round(sum(elerity)/len(elerity),3) if len(elerity)>0 else None)
                    celer['text']='Average Correct Celerity: %s'%(round(sum(celerity)/len(celerity),3) if len(celerity)>0 else None)
                    ieler['text']='Average Incorrect Celerity: %s'%(round(sum(ielerity)/len(ielerity),3) if len(ielerity)>0 else None)
                    root.update()
            else:
                answerline['state']='disabled'
                enterans['state']='disabled'
                root.unbind("<Return>")
                fans=bonfalist[bonnum][subbonnum]
                actualans=bonalist[bonnum][subbonnum]
                if close_enough(givenans.lower(),fans,actualans.lower()):
                    curbpts+=10
                    subbonstatus.append(10)
                else:
                    if prompt(givenans,actualans):
                        curbpts+=10
                        subbonstatus.append(10)
                    else:
                        curbpts+=0
                        subbonstatus.append(0)
                reading=False
                aread=bonlist[bonnum][:subbonnum]
                allread=''
                for n,i in enumerate(aread):
                    allread+=i
                    allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
                qcanvas.itemconfigure(qtext,text=allread+bonlist[bonnum][subbonnum]+"\n\n"+bonalist[bonnum][subbonnum])
                read['state']='normal'
                root.bind('<\>', lambda event: readq())
                if subbonnum==2:
                    bonstatus.append(subbonstatus)
                    subbonstatus=[]
                    bon+=1
                    bpts+=curbpts
                    bagels[(30-curbpts)//10]+=1
                    bonct['text']='Bonuses: %s'%(bon)
                    bonuspts['text']='Bonus Points: %s'%(bpts)
                    ppb['text']='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2))
                    tttb['text']='30s/20s/10s/0s: %s'%('/'.join(str(i) for i in bagels))
                    root.update()
                    if tuorbon==2:
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
        global reading,buzzed,tunum,dead,ansalrgiven,qskipped,bonnum,subbonnum,curbpts,tustatus,bonstatus,subbonstatus,tuwd
        if dead or ansalrgiven:
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
            elif tuorbon==1:
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
            elif tuorbon==1:
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
    answerline.grid(row=0,column=3,padx=(5,5))
    buzzer.grid(row=0,column=2,padx=(5,5))
    qbt.grid(row=0,column=1,padx=(5,5))
    lbt.grid(row=0,column=2)
    root.bind('<Escape>',lambda event:backtohomescreen())
    root.bind('<Control-w>',lambda event:leavereader())
    root.focus_force()
    root.mainloop()
def prompt(gans,aans):
        if gans.strip()=='idk' or gans.strip()=='' or (gans.strip()=="n" and aans!="n"):
            return False
        return messagebox.askyesno("Were you correct?","Were you correct? (Press y/n)\nYour answer: %s\nActual answer: %s"%(gans,aans))
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
    if enchant.utils.levenshtein(given,normalans)<min(3,len(normalans)//2):
        return True
    return False
def check_if_buzz_at_eotu():
    global dead,tu,tuct,tossuppts,ppg,ptnct,root,buzzer,qcanvas,qtext,reading,tuwd,tbrn
    if reading==False and buzzed==False:
        if ttbb==2:
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
    global dead,bon,bonct,bonuspts,ppb,tttb,curbpts,answerline,reading,tbrn,bagels,bpts,subbonstatus,bonstatus
    ans=is_this_correct.get()
    if ans!="":
        answerline.delete(0,len(ans))
        if close_enough(ans.lower(),bonfalist[bonnum][subbonnum],bonalist[bonnum][subbonnum].lower()):
            curbpts+=10
            subbonstatus.append(10)
        else:
            if prompt(ans,bonalist[bonnum][subbonnum]):
                curbpts+=10
                subbonstatus.append(10)
            else:
                curbpts+=0
                subbonstatus.append(0)
    if reading==False and ansalrgiven==False:
        dead=True
        subbonstatus.append(0)
        if ttbb==2 and subbonnum==2:
            tbrn=0
        if subbonnum==2:
            bonstatus.append(subbonstatus)
            subbonstatus=[]
            bon+=1
            bagels[(30-curbpts)//10]+=1
            bpts+=curbpts
            bonct['text']='Bonuses: %s'%(bon)
            bonuspts['text']='Bonus Points: %s'%(bpts)
            ppb['text']='PPB: %s'%(0.0 if bon==0 else round(bpts/bon,2))
            tttb['text']='30s/20s/10s/0s: %s'%('/'.join(str(i) for i in bagels))
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
    global pm,qlen,curq
    current_q = tulist[tunum]
    powermark=current_q.find("(*)")
    words=current_q.split()
    if powermark>-1:
        for i in range(len(words)):
            j=words[i].find("(*)")
            if j!=-1:
                if words[i]=="(*)":
                    words.pop(i)
                    pm=i-1
                    words[i-1]=words[i-1]+" (*)"
                    break
                elif j==(len(words[i])-3):
                    pm=i
                    words[i]=words[i].replace("(*)"," (*)")
                    break
                elif j==0:
                    pm=i-1
                    words[i]=words[i][3:]
                    words[i-1]=words[i-1]+" (*)"
                    break
                elif j>=0:
                    pm=i
                    n=words[i][j+3:]
                    words[i]=words[i][:j]+" (*)"
                    words.insert(i+1,n)
                    break
    else:
        pm=-1
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
    if subbonnum==0:
        breakspace=current_q[subbonnum][:current_q[subbonnum].find("\n")].count(' ')
        if breakspace>=0:
            bonwords[breakspace+1]='\n'+bonwords[breakspace+1]
    aread = current_q[:subbonnum]
    allread=''
    for n,i in enumerate(aread):
        allread+=i
        allread+="\n\n"+bonalist[bonnum][n]+"\n\n"
    iterbon(allread,bonwords, 1, window,canvas,question_txt,timeint)
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
def stripemsub(s):
    s=s.replace("<em>","")
    s=s.replace("</em>","")
    s=s.replace("<sub>","")
    s=s.replace("</sub>","")
    return s
def fetchqs(cats,subcats,diffs,tours,tuorbon):
    global tulist,tualist,tufalist,bonlist,bonalist,bonfalist,tutourlist,bontourlist
    catids={"Current Events":26, "Fine Arts":21, "Geography":20, "History":18, "Literature":15, "Mythology":14, "Philosophy":25, "Religion":19, "Science":17, "Social Science":22, "Trash":16}
    subcatids={'American Current Events':40, 'Other Current Events':42, 'American Fine Arts':35, 'Audiovisual Fine Arts':27, 'Auditory Fine Arts':8, 'British Fine Arts':45, 'European Fine Arts':50, 'Opera':77, 'Visual Fine Arts':2, 'World Fine Arts':43, 'Other Fine Arts':25, 'American Geography':38, 'World Geography':44, 'American History':13, 'British History':6, 'Classical History':16, 'European History':24, 'World History':20, 'Other History':28, 'American Literature':4, 'British Literature':22, 'Classical Literature':30, 'European Literature':1, 'World Literature':12, 'Other Literature':29, 'American Mythology':33, 'Chinese Mythology':47, 'Egyptian Mythology':65, 'Greco-Roman Mythology':58, 'Indian Mythology':46, 'Japanese Mythology':48, 'Norse Mythology':63, 'Other East Asian Mythology':49, 'Other Mythology':54, 'American Philosophy':39, 'Classical Philosophy':61, 'East Asian Philosophy':52, 'European Philosophy':66, 'Other Philosophy':74, 'American Religion':31, 'Christianity':57, 'East Asian Religion':51, 'Islam':68, 'Judaism':69, 'Other Religion':62, 'American Science':36, 'Biology':14, 'Chemistry':5, 'Computer Science':23, 'Math':26, 'Physics':18, 'World Science':37, 'Other Science':10, 'American Social Science':34, 'Anthropology':76, 'Economics':56, 'Linguistics':75, 'Political Science':64, 'Psychology':71, 'Sociology':73, 'Other Social Science':60, 'American Trash':32, 'Movies':72, 'Music':67, 'Sports':55, 'Television':70, 'Video Games':53, 'Other Trash':59}
    t,tt,ttt,tttt,bbb,bbbb,bbbbb,bbbbbb=[],[],[],[],[],[],[],[]
    clist=set()
    sclist=set()
    dlist=set(diffs)
    tlist=set()
    for i in cats:
        clist.add(catids[i])
    for i in subcats:
        sclist.add(subcatids[i])
    for i in tours:
        tlist.add(tourids[i][0])
    if tuorbon==0 or tuorbon==2:
        for i in data["data"]["tossups"]:
            if i["text"]!="[missing]" and i["answer"]!="[missing]" and i["tournament_id"]:
                if ((i["category_id"] in clist or i["subcategory_id"] in sclist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist)) and i["text"] not in tulist:
                    z=i["text"]
                    z=stripemsub(z)
                    t.append(z)
                    a=i["answer"]
                    a=stripemsub(a)
                    if a.find("&lt")>=0:
                        a=a[:a.find("&lt")]
                    elif a.find("<")>=0:
                        a=a[:a.find("<")]
                    ttt.append(a)
                    c=i["formatted_answer"]
                    c=stripemsub(c)
                    if c.find("&lt")>=0:
                        c=c[:c.find("&lt")]
                    tt.append(c)
                    tttt.append((i["tournament"]["name"],i["tournament"]["difficulty_num"]))
        if len(t)>0:
            tus=list(zip(t,tt,ttt,tttt))
            random.shuffle(tus)
            t,tt,ttt,tttt=zip(*tus)
            tulist.extend(list(t))
            tufalist.extend(list(tt))
            tualist.extend(list(ttt))
            tutourlist.extend(list(tttt))
    if tuorbon==1 or tuorbon==2:
        for i in data["data"]["bonuses"]:
            if len(i["texts"])!=0 and len(i["answers"])!=0 and i["tournament_id"]:
                b=i["texts"].copy()
                b[0]=i["leadin"]+"\n"+b[0]
                if((i["category_id"] in clist or i["subcategory_id"] in sclist) and (i["tournament"]["difficulty_num"] in dlist or i["tournament_id"] in tlist))and b not in bonlist:
                    for n,j in enumerate(b):
                        b[n]=stripemsub(j)
                    bbb.append(b)
                    a=i["answers"]
                    for n,j in enumerate(a):
                        k=stripemsub(j)
                        if k.find("&lt")>=0:
                            a[n]=k[:k.find("&lt")]
                        elif j.find("<")>=0:
                            a[n]=k[:k.find("<")]
                    bbbbb.append(a)
                    c=i["formatted_answers"]
                    for n,j in enumerate(c):
                        k=stripemsub(j)
                        if k.find("&lt")>=0:
                            k=k[:k.find("&lt")]
                        c[n]=k
                    bbbb.append(c)
                    bbbbbb.append((i["tournament"]["name"],i["tournament"]["difficulty_num"]))
        if len(bbb)>0:
            bons=list(zip(bbb,bbbb,bbbbb,bbbbbb))
            random.shuffle(bons)
            bbb,bbbb,bbbbb,bbbbbb=zip(*bons)
            bonlist.extend(list(bbb))
            bonfalist.extend(list(bbbb))
            bonalist.extend(list(bbbbb))
            bontourlist.extend(list(bbbbbb))
settourlist()
setup()
if (cc,sscc,dd,ttoouurr,ttbb,tthhyymmee)!=(None,None,None,None,None,None):
    if ttbb<2:
        tbrn=ttbb
    else:
        tbrn=0
    fetchqs(cc,sscc,dd,ttoouurr,ttbb)
    qscreen(ttbb,tthhyymmee)