# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

numbers_count = int(input())
positives = list()
negatives = list()
sum_of_negatives = 0

for line in range(numbers_count):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)
        sum_of_negatives += number

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum_of_negatives}")
