import tkinter as tk
from tkinter import filedialog,colorchooser,font,messagebox

class TextEditor:
    def __init__(self,root):
        self.root = root
        self.root.title("Notepad Classic")
        self.filename = None
        self.current_font_family = "Arial"
        self.currect_font_size = 12
        self.text_font = font.Font(family=self.current_font_family,size=self.currect_font_size)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu.tk.Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="Open",command=self.open_file)
        self.file_menu.add_command(label="Save",command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.root.quit)
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        self.bold_btn = tk.Button(self.toolbar,text="Bold",command=self.make_bold)
        self.bold_btn.pack(side=tk.LEFT,padx=x)
        
        self.italic_btn = tk.Button(self.toolbar,text="Italic",command=self.make_italic)
        self.italic_btn.pack(side=tk.LEFT,padx=2)
        self.underline_btn = tk.Button(self.toolbar,text="Underline",command=self.make_underline)
        self.underline_btn_btn.pack(side=tk.LEFT,padx=2)
        self.increase_font_btn = tk.Button(self.toolbar,text="A+",command=self.increase_font)
        self.increase_font_btn.pack(side=tk.LEFT,padx=2)
        self.deacrease_font_btn = tk.Button(self.toolbar,text="A-",command=self.deacrease_font)
        self.deacrease_font_btn.pack(side=tk.LEFT,padx=2)

        self.color_btn = tk.Button(self.toolbar, text="Text Color", command=self.change_text_color)
        self.color_btn.pack(side=tk.LEFT, padx=2)

        self.bgcolor_btn = tk.Button(self.toolbar, text="BG Color", command=self.change_bg_color)
        self.bgcolor_btn.pack(side=tk.LEFT, padx=2)

        self.text_area = tk.Text(self.root, wrap="word", font=self.text_font, undo=True)
        self.text_area.pack(expand=1, fill=tk.BOTH)
        
        self.text_area.tag_configure("bold", font=(self.current_font_family, self.current_font_size, "bold"))
        self.text_area.tag_configure("italic", font=(self.current_font_family, self.current_font_size, "italic"))
        self.text_area.tag_configure("underline", font=(self.current_font_family, self.current_font_size, "underline"))
    def open_file(self):
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file:
        self.filename = file
        with open(file, "r", encoding="utf-8") as f:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f.read())
    def save_file(self):
        if not self.filename:
            file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Document", "*.txt"), ("All Files", "*.*")]))
            if not file:
                return
            self.filename = file
        with open(self.filename, "w",encoding="utf-8") as f:
            f.write(self.text_area.get(1.0,tk.END))
        
