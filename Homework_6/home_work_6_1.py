message = input("Enter a sentence: ")
words = message.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count:")
for word, count in word_count.items():
    print(f"{word}: {count}")