import tkinter as tk
from tkinter import messagebox
from .binary_tree import AnimalTree
from .data_loader import DataLoader

class AnimalOrganizerGUI:
    def __init__(self):
        self.tree = AnimalTree()
        DataLoader.load_animals("animals.csv", self.tree)
        self.window = tk.Tk()
        self.window.title("Animal Organizer")

        self.label = tk.Label(self.window, text="Enter Animal Name:")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.search_button = tk.Button(self.window, text="Search", command=self.search_animal)
        self.search_button.pack()

    def search_animal(self):
        name = self.entry.get()
        animal = self.tree.search(name)
        messagebox.showinfo("Search Result", str(animal) if animal else "Animal not found.")

    def run(self):
        self.window.mainloop()
