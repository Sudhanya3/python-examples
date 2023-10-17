from tkinter import *
import tkinter as tk

input = ""
def enter_text(n):
    global input
    input = input + str(n)
    equation.set(input)

def calculate():
    try:
        global input
        result = str(eval(input))
        equation.set(result)
        input = ""
    except:
        equation.set(" ERROR ")
        input = ""

def clear_text():
    global input
    input = ""
    equation.set("")


window = tk.Tk()
window.geometry("400x300")
window.title("My Calculator")
equation = tk.StringVar() 

# text_field = tk.Text(window, width=35, height=3, font=("Calibri", 18))
text_field = Entry(window, textvariable=equation, width=30, font=("Calibri", 18))
text_field.grid(columnspan=4)
#numbered buttons
btn_7 = tk.Button(window, text="7", command=lambda:enter_text(7), height=2, width=3, font=("Calibri", 13))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(window, text="8", command=lambda:enter_text(8), height=2, width=3, font=("Calibri", 13))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(window, text="9", command=lambda:enter_text(9), height=2, width=3, font=("Calibri", 13))
btn_9.grid(row=2, column=2)
btn_4 = tk.Button(window, text="4", command=lambda:enter_text(4), height=2, width=3, font=("Calibri", 13))
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(window, text="5", command=lambda:enter_text(5), height=2, width=3, font=("Calibri", 13))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(window, text="6", command=lambda:enter_text(6), height=2, width=3, font=("Calibri", 13))
btn_6.grid(row=3, column=2)
btn_1 = tk.Button(window, text="1", command=lambda:enter_text(1), height=2, width=3, font=("Calibri", 13))
btn_1.grid(row=4, column=0)
btn_2 = tk.Button(window, text="2", command=lambda:enter_text(2), height=2, width=3, font=("Calibri", 13))
btn_2.grid(row=4, column=1)
btn_3 = tk.Button(window, text="3", command=lambda:enter_text(3), height=2, width=3, font=("Calibri", 13))
btn_3.grid(row=4, column=2)
btn_0 = tk.Button(window, text="0", command=lambda:enter_text(0), height=2, width=3, font=("Calibri", 13))
btn_0.grid(row=5, column=1)
# symbolized buttons
btn_plus = tk.Button(window, text="+", command=lambda:enter_text("+"), height=2, width=3, font=("Calibri", 13))
btn_plus.grid(row=2, column=3)
btn_minus = tk.Button(window, text="-", command=lambda:enter_text("-"), height=2, width=3, font=("Calibri", 13))
btn_minus.grid(row=3, column=3)
btn_multiply = tk.Button(window, text="*", command=lambda:enter_text("*"), height=2, width=3, font=("Calibri", 13))
btn_multiply.grid(row=4, column=3)
btn_division = tk.Button(window, text="%", command=lambda:enter_text("%"), height=2, width=3, font=("Calibri", 13))
btn_division.grid(row=5, column=0)
btn_clear = tk.Button(window, text="C", command= clear_text, height=2, width=3, font=("Calibri", 13))
btn_clear.grid(row=5, column=2)
btn_equal = tk.Button(window, text="=", command= calculate, height=2, width=3, font=("Calibri", 13))
btn_equal.grid(row=5, column=3)


window.mainloop()