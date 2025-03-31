import tkinter as tk
from tkinter import messagebox
import pickle

class TextListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text List App")
        
        self.text_list = []
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add", command=self.add_text)
        self.add_button.pack(pady=5)
        
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
        
        self.save_button = tk.Button(root, text="Save", command=self.save_list)
        self.save_button.pack(pady=5)
    
    def add_text(self):
        text = self.entry.get()
        if text:
            self.text_list.append(text)
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Text cannot be empty")
    
    def save_list(self):
        with open("text_list.pkl", "wb") as f:
            pickle.dump(self.text_list, f)
        messagebox.showinfo("Saved", "List saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextListApp(root)
    root.mainloop()
