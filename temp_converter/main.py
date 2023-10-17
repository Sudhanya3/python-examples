from tkinter import *
import tkinter as tk
from functools import partial

temp_type = "Celsius" 

def temp_store(type):
    global temp_type
    temp_type = type

def temp_converter(output, t):
    temp = t.get()

    global temp_type

    if temp_type == "Fahrenheit":
        c = float((float(temp) - 32) * 5 / 9)
        output.config(text = "%.1f Celsius" % c)
    if temp_type == "Celsius":
        f = float((float(temp) * 9 / 5) + 32)
        output.config(text = "%.1f Fahrenheit" % f)

    return

window = Tk()
window.geometry("500x300")
window.title("Temperature Converter")

temperature = tk.StringVar()
var = tk.StringVar()

input_temp_label = tk.Label(window, text="Enter your Temperature", background="SkyBlue1")
input_temp_entry = Entry(window, textvariable=temperature)
input_temp_label.grid(row=1)
input_temp_entry.grid(row=1, column=1)
result_label = tk.Label(window)
result_label.grid(row= 4, columnspan=2)

dropDown = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(window, var, *dropDown, 
            command = temp_store)
var.set(dropDown[0])
drop_down.grid(row=1, column=2)

temp_converter = partial(temp_converter, result_label, temperature)
result_button = tk.Button(window, text="Convert", command=temp_converter)
result_button.grid(row=2, columnspan=2)

window.mainloop()