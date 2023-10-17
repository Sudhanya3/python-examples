import tkinter as tk

# Create a root window
root = tk.Tk()

# Create a label widget with the text "Hello, World!"
label = tk.Label(root, text="*** Welcome to Python ***")


# Pack the label into the root window
label.pack()

# Start the Tkinter main loop
root.mainloop()