import csv
from .animal import Animal

class DataLoader:
    @staticmethod
    def load_animals(filepath, tree):
        """Loads animals from a CSV file into the binary tree."""
        try:
            with open(filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    animal = Animal(
                        name=row['name'],
                        species=row['species'],
                        animal_type=row['animal_type'],
                        diet=row['diet'],
                        extra=row['extra']
                    )
                    tree.insert(animal)  # Assuming `insert()` method exists in AnimalTree
        except Exception as e:
            print(f"Error loading animals: {e}")
