# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".

words = input().split()
palindrome_word = input()

# palindrome_list = []
# for word in words:
#     if word == word[::-1]:
#         palindrome_list.append(word)

palindrome_list = [word for word in words if word == word[::-1]]
palindrome_word_found = [palindrome for palindrome in palindrome_list].count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_word_found} times")
