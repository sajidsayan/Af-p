import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Classic Calculator")
root.config(bg="#2E2E2E")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=3, relief="ridge", justify='right', bg="#1C1C1C", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, pady=15, padx=15, sticky="we")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

btn_bg = "#4B4B4B"
btn_fg = "white"
op_bg = "#FF9500"
op_fg = "white"
eq_bg = "#28A745"
eq_fg = "white"
clr_bg = "#D32F2F"
clr_fg = "white"

row = 1
col = 0

for button_text in buttons:
    if button_text == "C":
        bg_color = clr_bg
        fg_color = clr_fg
    elif button_text == "=":
        bg_color = eq_bg
        fg_color = eq_fg
    elif button_text in ['/', '*', '-', '+']:
        bg_color = op_bg
        fg_color = op_fg
    else:
        bg_color = btn_bg
        fg_color = btn_fg
    
    button = tk.Button(root, text=button_text, font=("Arial", 20), width=5, height=2,
                       bg=bg_color, fg=fg_color, activebackground="#666666", activeforeground="white", borderwidth=0)
    button.grid(row=row, column=col, padx=6, pady=6)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
