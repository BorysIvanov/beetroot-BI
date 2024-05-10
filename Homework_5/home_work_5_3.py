largest_palindrome = 0
x = 999

while x >= 100:
    y = 999
    while y >= 100:
        operate = x * y
        if str(operate) == str(operate)[::-1] and operate > largest_palindrome:
            largest_palindrome = operate
        y -= 1
    x -= 1

print(f"The largest palindrome is: {largest_palindrome}")


for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        product = i * j
        if product <= largest_palindrome:
            break
        if str(product) == str(product)[::-1]:
            largest_palindrome = product


