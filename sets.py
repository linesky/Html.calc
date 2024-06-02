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
        self.root.title("set")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        self.text_area2 = tk.Text(self.root, height=10, width=50)
        self.text_area2.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="refresh", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="save", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="export", command=self.copy_file)
        self.copy_button.pack(pady=5)
        self.text_area.delete(1.0, tk.END)
        self.text_area2.delete(1.0, tk.END)
        self.text_area.insert(tk.END,"ver=1.0",True)

        try:
            
            result = subprocess.check_output("set", stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area2.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if 0==0:
                
                self.text_area2.insert(tk.END,f"Error executing command:\n{e.output}")
    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            #self.text_area2.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                a=0
                #self.text_area2.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        self.text_area2.delete(1.0, tk.END)
        try:
            
            result = subprocess.check_output("set", stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area2.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if 0==0:
                
                self.text_area2.insert(tk.END,f"Error executing command:\n{e.output}")
    
    def run_kernel(self):
        
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        txts=self.text_area.get("1.0", "end-1c")
        f1=open(filename,"w")
        f1.write(txts)
        f1.close()
        
    def copy_file(self):
        
        
        txts=self.text_area.get("1.0", "end-1c")
        txts=txts.replace("\r","\n")
        txts=txts.replace("\n\n","\n")
        txts2=txts.split("\n")
        for tx1 in txts2:
            txts3=tx1.split(";")
            for tx2 in txts3:
                tx2=tx2.strip()
                if tx2!="":
                    self.execute_command("export "+tx2,True)


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
