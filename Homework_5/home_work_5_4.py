zoo = [
    ["monkey", "tiger", "elephant"],
    ["frog", "snake"],
    ["owl", "pigeon"],
    ["hamster", "mouse", "hedgehog"]

]
for animals in zoo:
    for animal in animals:
        (animal.count("a") and print(animal))