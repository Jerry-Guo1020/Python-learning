import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    print(entry_int.get())
    output_string.set(km_output)

window = ttk.Window(themename='journal')
# 设置一些参数
window.title("2025年9月18日")
window.geometry("300x150")


# 标题
title_label = ttk.Label(master= window, text="今天我很开心", font= 'Calibri 24 bold')
title_label.pack()

# 输入框
input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entry_int)
button = ttk.Button(master= input_frame, text="convert", command=convert)

input_frame.pack()
entry.pack(pady=10)
button.pack(side = "right")

# 输出
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= 'Output', font='Calibri 24', textvariable=output_string)
output_label.pack()

# 跑起来
window.mainloop()