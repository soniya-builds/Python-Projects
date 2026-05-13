import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(
    root,
    font=('calibri', 50, 'bold'),
    background='pink',
    foreground='black'
)
label.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p\n%d-%m-%Y')
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()