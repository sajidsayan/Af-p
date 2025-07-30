import tkinter as tk

prices = {
    "Butter Chicken": 430,
    "Mix Masalla": 640,
    "Burger": 140,
    "Pizza": 240,
    "Coca Cola Big Bottle": 20
}

conversion = {
    "INR": 1,
    "BDT": 1.35,
    "USD": 0.012
}

currency_logo = {
    "INR": "₹",
    "BDT": "৳",
    "USD": "$"
}

entries = {}

def place_order():
    total = 0
    for item in prices:
        try:
            qty = int(entries[item].get())
            total += prices[item] * qty
        except:
            pass
    cur = currency_var.get()
    converted = total * conversion[cur]
    result_label.config(text=f"Total: {currency_logo[cur]}{converted:.2f}")

root = tk.Tk()
root.title("Restaurant Bill Management")
root.geometry("300x400")

tk.Label(root, text="Restaurant Order Management", font=("Arial", 13, "bold")).pack(pady=10)

for item in prices:
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text=f"{item} (₹{prices[item]}):", width=20, anchor="w").pack(side="left")
    ent = tk.Entry(frame, width=5)
    ent.insert(0, "0")
    ent.pack(side="right")
    entries[item] = ent

frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Currency:", width=20, anchor="w").pack(side="left")

currency_var = tk.StringVar()
currency_var.set("INR")
currency_menu = tk.OptionMenu(frame, currency_var, "INR", "BDT", "USD")
currency_menu.pack(side="right")

tk.Button(root, text="Place Order", command=place_order).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
