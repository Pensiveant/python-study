import tkinter as tk

window = tk.Tk()
window.title('test')
window.geometry('500x200')

l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
l.pack()
window.mainloop()
 
