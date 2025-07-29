import tkinter as tk

def convert_length():
    try:
        inches_value = float(inches_entry.get())
        cm_value = inches_value * 2.54
        result_string_var.set(f"Result: {cm_value:.2f} cm")
    except ValueError:
        result_string_var.set("Please enter a valid number")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x250")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

font_style_normal = ('Helvetica', 12)
font_style_bold = ('Helvetica', 14, 'bold')

prompt_label = tk.Label(
    main_frame,
    text="Enter length in inches:",
    font=font_style_normal
)
prompt_label.pack(pady=10)

inches_entry = tk.Entry(
    main_frame,
    width=15,
    font=font_style_normal,
    justify='center',
    relief=tk.SOLID,
    bd=1
)
inches_entry.pack(pady=5)
inches_entry.focus()

convert_button = tk.Button(
    main_frame,
    text="Convert to Centimeters",
    font=('Helvetica', 12, 'bold'),
    command=convert_length
)
convert_button.pack(pady=15)

result_string_var = tk.StringVar()
result_label = tk.Label(
    main_frame,
    textvariable=result_string_var,
    font=font_style_bold
)
result_label.pack(pady=10)

root.mainloop()
