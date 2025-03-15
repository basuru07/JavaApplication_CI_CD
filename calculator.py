import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))  # eval() will evaluate the mathematical expression
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to update the entry field
def button_click(value):
    current = entry_var.get()
    current += str(value)
    entry_var.set(current)

# Function to clear the entry field
def clear():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to store the value of the entry field
entry_var = tk.StringVar()

# Create the entry field
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, font=("Arial", 20), bd=5, relief="raised", command=lambda: evaluate_expression(entry_var.get())).grid(row=row, column=col, sticky="nsew")
    elif text == "C":
        tk.Button(root, text=text, font=("Arial", 20), bd=5, relief="raised", command=clear).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, font=("Arial", 20), bd=5, relief="raised", command=lambda value=text: button_click(value)).grid(row=row, column=col, sticky="nsew")

# Configure grid to make buttons expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
