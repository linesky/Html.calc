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
        self.root.title("pci")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        
        # Botões
        
        self.run_button = tk.Button(self.root, text="save", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="run", command=self.copy_file)
        self.copy_button.pack(pady=5)
        self.text_area.delete(1.0, tk.END)
        
        try:
            
            result = subprocess.check_output("lspci", stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if 0==0:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        
        filename = tk.filedialog.askopenfilename(title="Select file")
        f1=open(filename,"r")
        txts=f1.read()
        
        f1.close()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, txts,True)
        
    
    def run_kernel(self):
        
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        txts=self.text_area.get("1.0", "end-1c")
        f1=open(filename,"w")
        f1.write(txts)
        f1.close()
        
        
        
    def copy_file(self):
        
        
        self.text_area.delete(1.0, tk.END)
        self.execute_command("lspci",True)

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
