from tkinter import *
import tkinter as tk

def bmi_calculator():
    weight_input = float(weight_entry.get())
    height_input = float(height_entry.get())
    bmi = float(weight_input / (height_input * height_input))
    result_label.config(text = "BMI: %.2f" % bmi)

    if bmi <= 18.4:
        indicator.config(text="You are Underweight, EAT MORE :/ ")
    if bmi >= 18.5 and bmi <= 24.9:
        indicator.config(text="You are Normal, KEEP IT UP :) ")

    if bmi >= 25.0 and bmi <= 39.9:
        indicator.config(text="You are Overweight, HIT THE GYM :( ")

    if bmi >= 40.0:
        indicator.config(text="You are Obese, BE CONSIDERATE OF YOUR HEALTH", background="SkyBlue1")
    
#creating a screen for calculation
screen = Tk()
screen.title("Adult and Child BMI Calculator")
screen.geometry("500x300")

# creating labels for weight and height
weight_label = tk.Label(screen, text="Weight (in kgs)")
weight_label.grid(row=1, column=1)
weight_entry = Entry(screen)
weight_entry.grid(row=1,column=2)
height_label = tk.Label(screen, text="Height (in mts)")
height_label.grid(row=2, column=1)
height_entry = Entry(screen)
height_entry.grid(row=2, column=2)

# calculation buttons
calculate_button = tk.Button(screen, text="Calculate", font=("Calibri", 14), command=bmi_calculator)
calculate_button.grid(row=3, column=2)
# clear_button = tk.Button(screen, text="Clear", font=("Calibri", 14), command=bmi_calculator)
# clear_button.grid(row=3, column=2)

result_label = tk.Label(screen, text="")
result_label.grid(row=4, column=2)

indicator = tk.Label(screen, text="")
indicator.grid(row=6, column=2)

indication_level = tk.Label(screen, text="")
indication_level.grid(row=7, column=2)

under_weight = tk.Label(screen, text="Underweight BMI Range : <=18.4 ", background="SkyBlue1")
under_weight.grid(row=9, column=2)
normal_weight = tk.Label(screen, text="Normal BMI Range : 18.5 - 24.9", background="Green1")
normal_weight.grid(row=10, column=2)
over_weight = tk.Label(screen, text="Overweight BMI Range : 25.0 - 39.9", background="Orange1")
over_weight.grid(row=11, column=2)
obese_weight = tk.Label(screen, text="Obese BMI Range : >= 40.0", background="Red1")
obese_weight.grid(row=12, column=2)

screen.mainloop()
