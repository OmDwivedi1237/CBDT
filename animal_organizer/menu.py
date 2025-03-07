from .binary_tree import AnimalTree
from .data_loader import DataLoader
from .animal import Animal

class Menu:
    def __init__(self):
        self.tree = AnimalTree()
        DataLoader.load_animals("animals.csv", self.tree)  # ✅ Corrected this call

    def run(self):
        while True:
            print("\n=== Animal Organizer Menu ===")
            print("1. Display Animals")
            print("2. Add an Animal")
            print("3. Remove an Animal")
            print("4. Search for an Animal")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.tree.display()  # Assuming display method exists
            elif choice == "2":
                self.add_animal()
            elif choice == "3":
                self.remove_animal()
            elif choice == "4":
                self.search_animal()
            elif choice == "5":
                print("Exiting program...")
                break
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
        self.tree.remove(name)  # Assuming remove method exists
        print(f"{name} has been removed.")

    def search_animal(self):
        name = input("Enter the name of the animal to search: ")
        found = self.tree.search(name)  # Assuming search method exists
        if found:
            print(f"Animal found: {found}")
        else:
            print("Animal not found.")
