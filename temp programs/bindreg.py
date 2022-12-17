import tkinter as tk

def func(event=None):
    tk.Label(main, text="Meow").pack()

main = tk.Tk()
bRoll = tk.Button(text = "Hello", command = func)
main.bind('r',func)
bRoll.bind('<Enter>',func)
bRoll.pack()

main.mainloop()