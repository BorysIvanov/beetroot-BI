import random

my_list_1 = []
my_list_2 = []
my_list_3 = []

while len(my_list_1) < 10 and len(my_list_2) < 10:
    my_list_1.append(random.randint(0, 10))
    my_list_2.append(random.randint(0, 10))
print("List 1: ", my_list_1)
print("List 2: ", my_list_2)

for number in my_list_1:
    if number in my_list_2:
        my_list_3.append(number)
print("List 3: ", set(my_list_3))
