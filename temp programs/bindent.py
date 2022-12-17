import tkinter as tk

class SimpleApp(object):
    def __init__(self, master, **kwargs):
        title = kwargs.pop('title')
        frame = tk.Frame(master, **kwargs)
        frame.grid()
        button = tk.Button(frame, text = 'search', command = self.search)
        button.grid()
        button.bind('<Return>', self.search)
        # uncomment if you want `<Return>` bound everywhere.
        # master.bind('<Return>', self.search)  
    def search(self,*args):
        print('searching...')

def basic():
    root = tk.Tk()
    app = SimpleApp(root, title = 'Hello, world')
    root.mainloop()

basic()