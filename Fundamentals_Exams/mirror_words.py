# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden
# word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a
# match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
# •	You will recive a string.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.

import re

input_text = input()
pairs = []
mirror_words = []

pattern = re.compile(r"([#@])(?P<word_one>([A-Za-z]){3,})\1{2}(?P<word_two>([A-Za-z]){3,})\1")
matches = re.finditer(pattern, input_text)
if matches:
    for match in matches:
        pairs.append([match["word_one"], match["word_two"]])

for pair in pairs:
    first_word, second_word = pair[0], pair[1]
    if second_word[::-1] == first_word:
        mirror_words.append(f"{first_word} <=> {second_word}")

if pairs:
    print(f"{len(pairs)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")
