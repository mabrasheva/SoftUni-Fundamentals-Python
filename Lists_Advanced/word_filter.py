# Using comprehension, write a program that receives some text, separated by space, and take only those words whose
# length is even. Print each word on a new line.

text = input().split()
result = [word for word in text if len(word) % 2 == 0]
print("\n".join(result))
