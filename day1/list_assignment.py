"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""
zoo = ["lion", "tiger", "elephant", "cheetah", "monkey"]
zoo.pop(3)
zoo.append("panther")
zoo.pop(0)
for animal in zoo:
    print(animal)
print(zoo[:])
for animal in zoo[:3]:
    print(animal)
print(zoo[:3])