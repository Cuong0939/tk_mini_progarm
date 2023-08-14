import tkinter as tk

window = tk.Tk()
window.title('Address Entry Form')

label = ["First Name:",
         "Last Name:",
         "Address Line 1:",
         "Address Line 2:",
         "City:",
         "State/Province:",
         "Postal Code:",
         "Country:"]
frame_upper = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=5)
for i in range (len(label)):
    title = tk.Label(master=frame_upper,text=label[i])
    entry = tk.Entry(master=frame_upper,width=50)
    title.grid(row=i,column=0,sticky="e")
    entry.grid(row=i,column=1)
frame_upper.pack()


frame_lower = tk.Frame(master=window,borderwidth=5,width=50)
btn1 = tk.Button(master=frame_lower,text="Clear")
btn2 = tk.Button(master=frame_lower,text="Submit")
btn1.pack(side=tk.RIGHT,padx=10,ipadx=10)
btn2.pack(side=tk.RIGHT,ipadx=10)
frame_lower.pack(fill=tk.X,ipadx=5,ipady=5)
window.mainloop()