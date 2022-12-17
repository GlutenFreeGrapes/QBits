import tkinter as tk
from tkinter import ttk
class BetterCheckMenu:
    def __init__(self,parent,vals,vars,**kwargs):
        self._popup = None
        self.text = None
        self._menubutton = []
        self.parent = parent
        for n,i in enumerate(vals):
            self._menubutton.append({'label':i,'variable':vars[n]})
        self.parent.bind('<Button-1>', self.on_popup)
        self.vals=vals
    def on_popup(self, event):
        if not self._popup and not self.text:
            x, y, height = self.parent.winfo_rootx(), self.parent.winfo_rooty(), self.parent.winfo_height()
            self._popup = tk.Toplevel(self.parent.master)
            self._popup.overrideredirect(True)
            self._popup.geometry('+{}+{}'.format(x, y + height))
            self.text=tk.Text(self._popup,width=max([len(str(i)) for i in self.vals])+5,background='#f0f0f0',height=10,)
            self.text.bind('<FocusOut>', self.destroy)
            self.text.pack(side='left')
            scroll=ttk.Scrollbar(self._popup,command=self.text.yview)
            scroll.pack(side='right',fill='y')
            self.text.configure(yscrollcommand=scroll.set)
            for i in self._menubutton:
                j=ttk.Checkbutton(self.text,text=i['label'],variable=i['variable'])
                self.text.window_create('e',window=j)
                self.text.insert('e','\n')
            self.text.configure(state='disabled',)
    def destroy(self,event):
        self.pb=((self.parent.winfo_rootx(),self.parent.winfo_rooty()),(self.parent.winfo_rootx()+self.parent.winfo_width(),self.parent.winfo_rooty()+self.parent.winfo_height()))
        if not (self.pb[0][0]<=self.parent.winfo_pointerxy()[0]<=self.pb[1][0] and self.pb[0][1]<=self.parent.winfo_pointerxy()[1]<=self.pb[1][1]):
            if self._popup:
                windo=self._popup
                self._popup=None
                windo.destroy()
            if self.text: 
                windo=self.text
                self.text=None
                windo.destroy()
        else:
            self.text.focus_force()
def sumbit():
    print('bt')
    # for i in vals:
    #     print(i,vars[i].get())
root=tk.Tk()
button=ttk.Menubutton(root,text='test')
button.grid()
root.update()
import random
vals=list(range(30))
random.shuffle(vals)
vars=[tk.BooleanVar() for i in vals]
button.menu=BetterCheckMenu(button,vals,vars)
button['menu']=button.menu
rand=ttk.Button(root,text='sdfgsdfgsdfg',command=sumbit)
rand.grid(column=1,row=0)
root.mainloop()