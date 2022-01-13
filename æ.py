class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
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
#radio buttons for tu, bonus, tu&bonus
#checkbox or smth for diffs
#text boxes for cats, subcats, etc
#some info box with lists of cats, subcats, etc
#quit button
import time, tkinter as tk
root=tk.Tk()
fram1=tk.Frame(root)
fram1.grid(row=0,column=0)
cats=tk.StringVar()
catl=tk.Label(fram1, text = 'Categories: ', font=('calibri',10, 'bold'))
catt=tk.Entry(fram1,textvariable = cats, font=('calibri',10,'normal'), width=50)
lcats=tk.Button(fram1, text='❓')
subcats=tk.StringVar()
subcatl=tk.Label(fram1, text = 'Subcategories: ', font=('calibri',10, 'bold'))
subcatt=tk.Entry(fram1,textvariable = subcats, font=('calibri',10,'normal'), width=50)
lsubcats=tk.Button(fram1, text='❓')
diffs=tk.StringVar()
diffl=tk.Label(fram1, text = 'Difficulties: ', font=('calibri',10, 'bold'))
difft=tk.Entry(fram1,textvariable = diffs, font=('calibri',10,'normal'), width=50)
ldiffs=tk.Button(fram1, text='❓')
tours=tk.StringVar()
tourl=tk.Label(fram1, text = 'Tournaments: ', font=('calibri',10, 'bold'))
tourt=tk.Entry(fram1,textvariable = tours, font=('calibri',10,'normal'), width=50)
ltours=tk.Button(fram1, text='❓')
catl.grid(row=0,column=0, sticky="e")
catt.grid(row=0,column=1, sticky="w")
lcats.grid(row=0,column=2, sticky="w")
CreateToolTip(lcats, text = 'Pick whatever categories you want, separated by commas. Leave blank for all. \nValid keywords for each category are displayed below: \nCurrent Events - "current events", "ce"\nFine Arts - "fine arts", "fa"\nGeography - "geography", "geo"\nHistory - "history", "hist"\nLiterature - "literature", "lit"\nMythology - "mythology", "myth", "m"\nPhilosophy - "philosophy", "philo", "p"\nReligion - "religion", "relig", "r"\nScience - "science", "sci"\nSocial Science - "social science", "social sci", "ss"\nTrash - "trash"\n\nEx. \n"current events" → only gives questions from current events\n"hist myth science" → gives questions from history, mythology, and science')
subcatl.grid(row=1,column=0, sticky="e")
subcatt.grid(row=1,column=1, sticky="w")
lsubcats.grid(row=1,column=2, sticky="w")
CreateToolTip(lsubcats, text = 'Current Events Subcategories: American Current Events - "american current events", "american ce", "amce"; Other Current Events - "other current events", "other ce", "oce"\n- Fine Arts Subcategories: American Fine Arts - "american fine arts", "american fa", "amfa"; Audiovisual Fine Arts - "audiovisual fine arts", "audiovisual fa", "avfa"; Auditory Fine Arts - "auditory fine arts", "auditory fa", "afa"; British Fine Arts - "british fine arts", "brit fine arts", "british fa", "britfa", "bfa"; European Fine Arts - "european fine arts", "euro fine arts", "european fa", "eurofa"; Opera - "opera"; Visual Fine Arts - "visual fine arts", "visual fa", "vfa"; World Fine Arts -  "world fine arts", "world fa", "wfa"; Other Fine Arts - "other fine arts", "other fa", "ofa"\n- Geography Subcategories: American Geography - "american geography", "american geo", "amgeo"; World Geography - "world geography", "world geo", "wgeo"\n- History Subcategories: American History - "american history", "american hist", "amhist"; British History - "british history", "brit history", "british hist", "brithist", "bhist"; European History - "european history", "euro history", "european hist", "eurohist"; Classical History - "classical history", "classical hist", "classhist"; World History - "world history", "world hist", "whist"; Other History - "other history", "other hist", "ohist"\n- Literature Subcategories: American Literature - "american literature", "american lit", "amlit"; British Literature - "british literature", "brit literature", "british lit", "britlit", "blit"; European Literature - "european literature", "euro literature", "european lit", "eurolit"; Classical Literature - "classical literature", "classical lit", "classlit"; World Literature - "world literature", "world lit", "wlit"; Other Literature - "other literature", "other lit", "olit"\n- Mythology Subcategories: American Mythology - "american mythology", "american myth", "ammyth"; Chinese Mythology - "chinese mythology", "chinese myth", "chmyth"; Egyptian Mythology - "egyptian mythology", "egyptian myth", "egyptmyth"; Greco-Roman Mythology - "greco roman mythology", "greco roman myth", "grmyth"; Indian Mythology - "indian mythology", "indian myth", "indmyth"; Japanese Mythology - "japanese mythology", "japanese myth", "jmyth"; Norse Mythology - "norse mythology", "norse myth"; Other East Asian Mythology - "other east asian mythology", "other east asian myth", "oeamyth"; Other Mythology - "other mythology", "other myth", "omyth"\n- Philosophy Subcategories: American Philosophy - "american philosophy", "american philo", "amphilo"; Classical Philosophy - "classical philosophy", "classical philo", "classphilo"; East Asian Philosophy - "east asian philosophy", "east asian philo", "eaphilo"; European Philosophy - "european philosophy", "euro philosophy", "european philo", "europhilo"; Other Philosophy - "other philosophy", "other philo", "ophilo"\n- Religion Subcategories: American Religion - "american religion", "american relig", "amrelig"; Christianity - "christianity"; East Asian Religion - "east asian religion", "east asian relig", "earelig"; Islam - "islam"; Judaism - "judaism"; Other Religion - "other religion", "other relig", "orelig"\n- Science Subcategories: American Science - "american science", "american sci", "amsci"; Biology - "biology", "bio"; Chemistry - "chemistry", "chem"; Computer Science - "computer science", "cs"; Math - "math"; Physics - "physics", "phys"; World Science - "world science", "world sci", "wsci"; Other Science - "other science", "other sci", "osci" \n- Social Science Subcategories: American Social Science - "american social science", "american ss", "amss"; Anthropology - "anthropology"; Economics - "economics", "econ"; Linguistics - "linguistics"; Political Science - "political science", "political sci", "polisci"; Psychology - "psychology", "psych"; Sociology - "sociology"; Other Social Science - "other social sci", "other ss", "oss"\n- Trash Subcategories: American Trash - "american trash", "amtrash"; Movies - "movies"; Music - "music"; Sports - "sports"; Television - "television", "tv"; Video Games - "video games", "vg"; Other Trash - "other trash", "otrash"')
diffl.grid(row=2,column=0, sticky="e")
difft.grid(row=2,column=1, sticky="w")
ldiffs.grid(row=2,column=2, sticky="w")
CreateToolTip(ldiffs, text = 'Pick whatever question difficulty levels you want, separated by commas. Leave blank for all. \nBelow is a list of all the difficulty level numbers and the difficulties they correspond to: \n1 → Middle School\n2 → Easy High School\n3 → Regular High School\n4 → Hard High School\n5 → National High School\n6 → Easy College\n7 → Regular College\n8 → Hard College\n9 → Open\n\nEx. \n"6" → questions with easy college difficulty\n"4-7" → questions with difficulty ranging from hard high school to regular college')
tourl.grid(row=3,column=0, sticky="e")
tourt.grid(row=3,column=1, sticky="w")
ltours.grid(row=3,column=2, sticky="w")
CreateToolTip(ltours, text = 'Pick whatever tournaments you want, separated by commas. Leave blank for all. \nYou may enter either simply years or simply packet names. \n\nEx. \n"2020 callisto" → 2020 CALLISTO packet\n"2020" → tournaments from 2020\n"pace" → all packets from PACE NSC tournaments')
fram2=tk.Frame(root)
fram2.grid(row=1,column=0)
timeo=tk.Label(fram2, text = 'Time between each word (ms): ', font=('calibri',10, 'bold'))
thyme = tk.Scale(fram2, from_=0, to=500, orient=tk.HORIZONTAL, length=600, tickinterval=50)
thyme.set(250)
timeo.grid(row=4,column=0, sticky="e")
thyme.grid(row=4,column=1, sticky="w")
fram3=tk.Frame(root)
fram3.grid(row=2,column=0)
tubon=tk.IntVar()
tuorbon=d1t=tk.Label(fram3, text = 'What kind of questions do you want? ', font=('calibri',10, 'bold'))
tu=tk.Radiobutton(fram3, text='Tossups only (TK)', variable=tubon, value=0)
bon=tk.Radiobutton(fram3, text='Bonuses only (PK)', variable=tubon, value=1)
tunbon=tk.Radiobutton(fram3, text='Tossups and bonuses', variable=tubon, value=2)
def submit():
    c=cats.get().strip().split(',')
    sc=subcats.get().strip().split(',')
    d=diffs.get().strip().split(',')
    t=tours.get().strip().split(',')
    tb=tubon.get()
    cat=[i.strip().lower().replace(' ','') for i in c if i.strip()!='']
    scat=[i.strip().lower().replace(' ','') for i in sc if i.strip()!='']
    diff=[i.strip().lower().replace(' ','') for i in d if i.strip()!='']
    tour=[i.strip().lower().replace(' ','') for i in t if i.strip()!='']
    print(cat,scat,diff,tour,tb)
    print(thyme.get())
sumbit=tk.Button(fram3,text = 'Go', command = submit)
quibt=tk.Button(fram3,text = 'Quit', command = quit)
tuorbon.grid(row=0,column=0, sticky="e")
tu.grid(row=0,column=1, sticky="w")
bon.grid(row=0,column=2, sticky="w")
tunbon.grid(row=0,column=3, sticky="w")
sumbit.grid(row=1,column=1)
quibt.grid(row=1,column=2)
root.mainloop()