import tkinter as tk

def display_next_q(window,canvas,question_txt):
    current_q = """Two wolves named "Greedy" and "Ravenous" devour the food that this deity doesn't eat. This deity can see far from his throne of Hlidskjalf, and has information brought to him by the ravens Huginn and Muninn. This deity hung on his spear Gungnir from the World Tree Yggdrasil in order to master the runes, and he gave up one of his eyes to drink from Mimir's well. He rides the eight-legged steed Sleipnir and will be swallowed whole by Fenrir at Ragnarok. For 10 points, name this owner of Valhalla, the chief god of the Norse pantheon."""
    
    powermark=current_q.find("(*)")
    tu=current_q.split()
    if powermark>-1:
        index=current_q[:powermark].count(" ")
        tu.pop(index)
        tu[index-1]+=" (*)"
    words = current_q.split()
    print(words,window,canvas,question_txt)
    i = 0

    iterative(words, 0, window,canvas,question_txt)

def iterative(words, i, window,canvas,question_txt):
    if i > len(words):
        return

    canvas.itemconfigure(question_txt, text=words[:i])
    i += 1
    window.after(150, lambda: iterative(words, i, window,canvas,question_txt))
window=tk.Tk()
frame=tk.Frame(window)
frame.grid(row=0,column=0)
canvas=tk.Canvas(frame, width=600, height=400, bg="black")
question_txt=canvas.create_text(300, 200,text="placeholder", width=600, fill="white",font=("calibri", 15))
canvas.pack()
display_next_q(frame,canvas,question_txt)
window.mainloop()