import random

my_list = []

while len(my_list) < 10:
    n = random.randint(0, 1000)
    my_list.append(n)

print(f"Random list {my_list}", "Largest is:", max(my_list))
