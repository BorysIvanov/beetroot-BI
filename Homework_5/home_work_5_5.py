experiments = [2, 11, 3, 5, 3, None,
               1, 9, 9, 8, 12, 7, 4, None,
               6, 2, 1, 3, 8, 3, 12, 4, 6, None,
               11, 2, 5, 7, 3, 9]

iterations = len(experiments) # 30 times

valid_iterations = []
for failed_iterations in experiments:
    if failed_iterations is not None:
        valid_iterations.append(failed_iterations) # 27 times

for drop in set(valid_iterations):
    probability = valid_iterations.count(drop) / iterations
    print(f"Dropped {drop}, Hits {valid_iterations.count(drop)} the probability is {probability.__round__(4)} %") # I have googled thos __method__ and it's beautifull


