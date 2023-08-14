import tkinter as tk

window = tk.Tk()
# def handle_keypress(event):
#     print(event.char)


# def handle_clickevent(event):
#     print("The button clicked!")

# button = tk.Button(master=window,text="Click")
# button.bind("<Button-1>",handle_clickevent)
# button.pack()    
# window.bind("<Key>",handle_keypress)

def handle_subevent():
    txt["text"] = str(int(txt["text"])-1)

def handle_addevent():
    txt["text"] = str(int(txt["text"])+1)





window.rowconfigure(0,minsize=50,weight=1)
window.columnconfigure([0,1,2],minsize=50,weight=1)


button_sub = tk.Button(master=window,text="-",command=handle_subevent)
txt = tk.Label(master=window,text="0",height=5,width=5)
button_add = tk.Button(master=window,text="+",command=handle_addevent)


button_sub.grid(row=0,column=0,sticky="nsew")
txt.grid(row=0,column=1)
button_add.grid(row=0,column=2,sticky="nsew")




window.mainloop()