# Create a class Zoo.
# It should have a class attribute called __animals that stores the total count of the animals in the zoo.
# The __init__ method should only receive the name of the zoo.
# There you should also create 3 empty lists (mammals, fishes, birds).
# The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species, adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}
# Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
# On the following n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species.
# At the end, print the info for that species and the total count of animals in the zoo.

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        __animals = len(self.mammals) + len(self.fishes) + len(self.birds)
        result += f"Total animals: {__animals}"
        return result


zoo = Zoo(input())
count = int(input())

for animal in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
