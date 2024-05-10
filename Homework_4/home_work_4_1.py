sample_str = input("Your text here: ")
if len(sample_str) < 2:
    print(" ")
else:
    print((sample_str[:2]) + (sample_str[-2:]))