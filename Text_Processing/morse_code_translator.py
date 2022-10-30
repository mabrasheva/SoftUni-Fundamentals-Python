# Write a program that translates messages from Morse code to English (capital letters).
# The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.

morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

code = input().split(" | ")
result = []
for word in code:
    word = word.split()
    result_word = []
    for letter in word:
        value = [i for i in morse_code_dict if morse_code_dict[i] == letter]
        result_word += value
    result_word = "".join(result_word)
    result.append(result_word)
print(*result)
