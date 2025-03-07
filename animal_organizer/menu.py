from .binary_tree import AnimalTree
from .data_loader import DataLoader
from .animal import Animal
from .gui import TreeVisualizer  # ✅ Added GUI for visualization

class Menu:
    def __init__(self):
        self.tree = AnimalTree()
        DataLoader.load_animals("animals.csv", self.tree)

    def run(self):
        while True:
            print("\n=== Animal Organizer Menu ===")
            print("1. Display Animals")
            print("2. Add an Animal")
            print("3. Remove an Animal")
            print("4. Search for an Animal")
            print("5. Exit")
            print("6. View Binary Tree Graphically")  # ✅ New option

            choice = input("Choose an option: ")
            if choice == "1":
                self.tree.display()
            elif choice == "2":
                self.add_animal()
            elif choice == "3":
                self.remove_animal()
            elif choice == "4":
                self.search_animal()
            elif choice == "5":
                print("Exiting program...")
                break
            elif choice == "6":  # ✅ Calls GUI
                self.view_tree_graphically()
            else:
                print("Invalid choice. Please try again.")

    def add_animal(self):
        name = input("Animal Name: ")
        species = input("Species: ")
        animal_type = input("Type (Mammal, Reptile, Bird, etc.): ")
        diet = input("Diet (Herbivore, Carnivore, Omnivore): ")
        extra = input("Extra Info: ")

        new_animal = Animal(name, species, animal_type, diet, extra)
        self.tree.insert(new_animal)
        print(f"{name} has been added!")

    def remove_animal(self):
        name = input("Enter the name of the animal to remove: ")
        self.tree.remove(name)
        print(f"{name} has been removed.")

    def search_animal(self):
        name = input("Enter the name of the animal to search: ")
        found = self.tree.search(name)
        if found:
            print(f"Animal found: {found}")
        else:
            print("Animal not found.")

    def view_tree_graphically(self):  # ✅ Calls the GUI
        print("Launching tree visualization...")
        TreeVisualizer(self.tree)
