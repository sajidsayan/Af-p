import tkinter as tk

def calculate_interest():
    try:
        principal_val = float(principal_entry.get())
        time_val = float(time_entry.get())
        rate_val = float(rate_entry.get())

        simple_interest = (principal_val * time_val * rate_val) / 100
        
        amount = principal_val * (pow((1 + rate_val / 100), time_val))
        compound_interest = amount - principal_val

        simple_interest_result_var.set(f'{simple_interest:.2f}')
        compound_interest_result_var.set(f'{compound_interest:.2f}')

    except ValueError:
        simple_interest_result_var.set("Invalid Input")
        compound_interest_result_var.set("Invalid Input")

root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("450x320")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

font_style = ('Helvetica', 12)
font_style_bold = ('Helvetica', 12, 'bold')

principal_label = tk.Label(main_frame, text="Principal Amount ($):", font=font_style)
principal_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=10)
principal_entry = tk.Entry(main_frame, width=20, font=font_style, relief=tk.SOLID, bd=1)
principal_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=10)

time_label = tk.Label(main_frame, text="Time Period (Years):", font=font_style)
time_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=10)
time_entry = tk.Entry(main_frame, width=20, font=font_style, relief=tk.SOLID, bd=1)
time_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=10)

rate_label = tk.Label(main_frame, text="Rate of Interest (%):", font=font_style)
rate_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=10)
rate_entry = tk.Entry(main_frame, width=20, font=font_style, relief=tk.SOLID, bd=1)
rate_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=10)

calculate_button = tk.Button(main_frame, text="Calculate", command=calculate_interest, font=font_style_bold)
calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

simple_interest_label = tk.Label(main_frame, text="Simple Interest:", font=font_style)
simple_interest_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
simple_interest_result_var = tk.StringVar()
simple_interest_result_label = tk.Label(main_frame, textvariable=simple_interest_result_var, font=font_style_bold)
simple_interest_result_label.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

compound_interest_label = tk.Label(main_frame, text="Compound Interest:", font=font_style)
compound_interest_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
compound_interest_result_var = tk.StringVar()
compound_interest_result_label = tk.Label(main_frame, textvariable=compound_interest_result_var, font=font_style_bold)
compound_interest_result_label.grid(row=5, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

main_frame.columnconfigure(1, weight=1)

root.mainloop()
