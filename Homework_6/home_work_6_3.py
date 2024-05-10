tuples_list = [(i, i ** 2) for i in range(1, 11)]

i_values, j_values = zip(*tuples_list)

print("Values of i:", i_values)
print("Values of j:", j_values)
