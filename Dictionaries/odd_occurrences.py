# Write a program that prints all elements from a given sequence of words that occur an odd number of
# times (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.

words = input().lower().split()
words_dict = {}
result = []

for word in words:
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for word, counter in words_dict.items():
    if counter % 2 != 0:
        result.append(word)

print(*result)
