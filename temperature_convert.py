import tkinter as tk

window = tk.Tk()

def temperature_convert():
    number = int(F_entry.get()) * (-17.22222)
    output_result['text'] = str(number) + " 'C"
    F_entry.delete(0,len(F_entry.get()))




F_entry = tk.Entry(master=window,width=10)
F_label = tk.Label(master=window,text="'F")
convert_btn = tk.Button(master=window,text="->",command=temperature_convert)
output_result = tk.Label(master=window,text="0 'C")


F_entry.pack(side=tk.LEFT)
F_label.pack(side=tk.LEFT)
convert_btn.pack(side=tk.LEFT)
output_result.pack(side=tk.LEFT)


window.mainloop()