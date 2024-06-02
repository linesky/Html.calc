import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("txt line number")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Botões
        self.build_button = tk.Button(self.root, text="open", command=self.build_kernel)
        self.build_button.pack(pady=5)

        

    

    def build_kernel(self):
        filename = tk.filedialog.askopenfilename(title="Select file")
        try:
            
            result = subprocess.check_output("gedit "+filename, stderr=subprocess.STDOUT, shell=True, text=True)
            
        except subprocess.CalledProcessError as e:
            result = subprocess.check_output("mousepad "+filename, stderr=subprocess.STDOUT, shell=True, text=True)
        


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
