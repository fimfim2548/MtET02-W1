import tkinter as tk

# ---------------- Window ----------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("360x550")
root.resizable(False, False)
root.configure(bg="#0f172a")

expression = ""

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Segoe UI", 28),
    bg="#1e293b",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="both", padx=15, pady=20, ipady=20)

# ---------------- Functions ----------------
def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def delete():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# ---------------- Button Style ----------------
button_font = ("Segoe UI", 16, "bold")

buttons = [
    ("AC", clear, "#ef4444"),
    ("DEL", delete, "#8b5cf6"),
    ("%", lambda: press("%"), "#06b6d4"),
    ("/", lambda: press("/"), "#06b6d4"),

    ("7", lambda: press("7"), "#334155"),
    ("8", lambda: press("8"), "#334155"),
    ("9", lambda: press("9"), "#334155"),
    ("*", lambda: press("*"), "#06b6d4"),

    ("4", lambda: press("4"), "#334155"),
    ("5", lambda: press("5"), "#334155"),
    ("6", lambda: press("6"), "#334155"),
    ("-", lambda: press("-"), "#06b6d4"),

    ("1", lambda: press("1"), "#334155"),
    ("2", lambda: press("2"), "#334155"),
    ("3", lambda: press("3"), "#334155"),
    ("+", lambda: press("+"), "#06b6d4"),

    ("0", lambda: press("0"), "#334155"),
    (".", lambda: press("."), "#334155"),
    ("=", calculate, "#f59e0b"),
]

frame = tk.Frame(root, bg="#0f172a")
frame.pack(expand=True, fill="both", padx=10, pady=10)

row = 0
col = 0

for text, command, color in buttons:
    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=button_font,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        bd=0,
        relief="flat"
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)

    col += 1
    if col == 4:
        col = 0
        row += 1

for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()