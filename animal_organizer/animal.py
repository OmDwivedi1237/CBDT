class Animal:
    def __init__(self, name, species, animal_type, diet, extra):
        self.name = name
        self.species = species
        self.animal_type = animal_type
        self.diet = diet
        self.extra = extra

    def __str__(self):
        return f"{self.name} - {self.species} ({self.animal_type}, {self.diet}) | {self.extra}"
