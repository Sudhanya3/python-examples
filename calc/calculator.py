import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current_text = screen.get()
        current_text += text
        screen.set(current_text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
entry_field = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry_field.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("x^n", 5, 0), ("square", 5, 1)
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font="lucida 20", relief="ridge", width=5, height=2)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
