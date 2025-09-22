import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title("window and widgets")
window.geometry("800x500")

# create widgets



# 首先会有一个文字内容 那么这个的主内容是要放在Window里面的 那么这个Window其实就是定义在这个框框这个，属于这个里面的内容
text = tk.Text(master= window)
text.pack()

# ttk widgets
label = ttk.Label(master= window, text= "this is a text")
label.pack()

# run
window.mainloop()
print("hello")  