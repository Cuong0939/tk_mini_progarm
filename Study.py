import tkinter as tk





# #Make frame for widget
# frame = tk.Frame()
# frame.pack()
# #Text object
# greeting = tk.Label(master=frame,text="Python rocks!")
# greeting.pack()

# #Entry object
# entry_text = tk.Entry(master=frame,fg="yellow",bg="blue",width=25)
# entry_text.pack()

# #Button object
# btn = tk.Button(master=frame,text='Click!',width=25,height=5,bg="blue",fg="yellow")
# btn.pack()

# frame_a = tk.Frame()
# label_a = tk.Label(master=frame_a,text="I'm in Frame a")
# label_a.pack()

# frame_b =tk.Frame()
# label_b = tk.Label(master=frame_b,text="I'm in Frame b")
# label_b.pack()



# frame_b.pack()
# frame_a.pack()


# border_effect = {
#     "flat" : tk.FLAT,
#     "sunken" : tk.SUNKEN,
#     "raised" : tk.RAISED,
#     "groove" : tk.GROOVE,
#     "ridge" : tk.RIDGE,
# }

# window = tk.Tk()

# for relief_name, relief in border_effect.items():
#     frame = tk.Frame(master=window,relief=relief,borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label=tk.Label(master=frame,text=relief_name)
#     label.pack()

# frame = tk.Frame()
# entry = tk.Entry(master=frame,width=50)
# entry.insert(0,"What is your name?")
# entry.pack()
# btn = tk.Button(master=frame,text="Click!",height=5,width=25)
# btn.pack()

# frame.pack()
# print(entry.get())
 
window = tk.Tk()
# frame1 = tk.Frame(master=window,width=200,height=100,bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)

# frame1 = tk.Frame(master=window,width=100,bg="yellow")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)

# frame1 = tk.Frame(master=window,width=50,bg="blue")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)


for i in range(3):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(3):
        frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label = tk.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack()
window.mainloop()