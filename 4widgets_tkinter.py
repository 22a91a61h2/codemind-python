import tkinter as tk
from tkinter import messagebox
# Create the main window
window = tk.Tk()
window.title("Widget Example")
# Create a Label widget
label = tk.Label(window, text="Hello, World!")
label.pack()
# Create a Button widget
def button_click():
messagebox.showinfo("Button Clicked", "Button was clicked!")
button = tk.Button(window, text="Click Me", command=button_click)
button.pack()
# Create an Entry widget
entry = tk.Entry(window)
entry.pack()
# Create a Checkbutton widget
var = tk.StringVar()
checkbutton = tk.Checkbutton(window, text="Check me", variable=var, onvalue="Checked", offvalue="Unchecked")
checkbutton.pack()
# Start the Tkinter event loop
window.mainloop()
