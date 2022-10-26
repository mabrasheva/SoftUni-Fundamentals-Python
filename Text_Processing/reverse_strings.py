# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings
# and prints each pair on a separate line in the format "{word} = {reversed_word}".
word = input()
while word != "end":
    reversed_word = word[::-1]
    # reversed_word = [i for i in reversed(word)]
    # reversed_word = "".join(reversed_word)
    print(f"{word} = {reversed_word}")
    word = input()
