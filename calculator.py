from tkinter import *

# Create the main window
window = Tk()
window.title("Calculator")

# Entry box
entry = Entry(window, width=25, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add a number to the entry
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Function to clear the entry
def clear():
    entry.delete(0, END)

# Function to calculate the answer
def equal():
    try:
        answer = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, answer)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Number Buttons
Button(window, text="7", padx=20, pady=20,
       command=lambda: button_click(7)).grid(row=1, column=0)

Button(window, text="8", padx=20, pady=20,
       command=lambda: button_click(8)).grid(row=1, column=1)

Button(window, text="9", padx=20, pady=20,
       command=lambda: button_click(9)).grid(row=1, column=2)

Button(window, text="/", padx=20, pady=20,
       command=lambda: button_click("/")).grid(row=1, column=3)

Button(window, text="4", padx=20, pady=20,
       command=lambda: button_click(4)).grid(row=2, column=0)

Button(window, text="5", padx=20, pady=20,
       command=lambda: button_click(5)).grid(row=2, column=1)

Button(window, text="6", padx=20, pady=20,
       command=lambda: button_click(6)).grid(row=2, column=2)

Button(window, text="*", padx=20, pady=20,
       command=lambda: button_click("*")).grid(row=2, column=3)

Button(window, text="1", padx=20, pady=20,
       command=lambda: button_click(1)).grid(row=3, column=0)

Button(window, text="2", padx=20, pady=20,
       command=lambda: button_click(2)).grid(row=3, column=1)

Button(window, text="3", padx=20, pady=20,
       command=lambda: button_click(3)).grid(row=3, column=2)

Button(window, text="-", padx=20, pady=20,
       command=lambda: button_click("-")).grid(row=3, column=3)

Button(window, text="0", padx=20, pady=20,
       command=lambda: button_click(0)).grid(row=4, column=0)

Button(window, text=".", padx=20, pady=20,
       command=lambda: button_click(".")).grid(row=4, column=1)

Button(window, text="=", padx=20, pady=20,
       command=equal).grid(row=4, column=2)

Button(window, text="+", padx=20, pady=20,
       command=lambda: button_click("+")).grid(row=4, column=3)

Button(window, text="Clear", padx=75, pady=10,
       command=clear).grid(row=5, column=0, columnspan=4)

window.mainloop()