import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}", fg="green")
    except ValueError:
        result_label.config(text="Please enter valid numbers", fg="red")

root = tk.Tk()
root.title("Product Calculator")
root.config(bg="#282c34")

tk.Label(root, text="Enter first number:", font=("Arial", 14), bg="#282c34", fg="#61dafb").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, font=("Arial", 14), bg="#3b3f4a", fg="white", insertbackground="white")
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:", font=("Arial", 14), bg="#282c34", fg="#61dafb").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, font=("Arial", 14), bg="#3b3f4a", fg="white", insertbackground="white")
entry2.grid(row=1, column=1, padx=10, pady=10)

calc_button = tk.Button(root, text="Calculate Product", font=("Arial", 14), bg="#61dafb", fg="#282c34", activebackground="#21a1f1", command=calculate_product)
calc_button.grid(row=2, column=0, columnspan=2, pady=15)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#282c34")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
