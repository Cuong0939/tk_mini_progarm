import tkinter as tk 
import random 




window = tk.Tk()
window.title("Rolling a six-sided die")


def random_generate_number():
    num = random.randint(1,6)
    txt["text"] = str(num)


txt = tk.Label(master=window,text="0")
txt.pack()

rolling_btn = tk.Button(master=window,text="Roll",width=50,command=random_generate_number)
rolling_btn.pack()




window.mainloop()