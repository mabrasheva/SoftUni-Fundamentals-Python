# Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of
# depression. And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those
# closest to you naturally get further, and those further from you, get closer.
# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin
# receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the
# pokemon).
# •	You must increase the value of all elements in the sequence which are less or equal to the removed element with the
# value of the removed element.
# •	You must decrease the value of all elements in the sequence which are greater than the removed element with the
# value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy
# the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is
# the removed element.
# The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
# Input
# •	On the first line of input, you will receive a sequence of integers, separated by spaces.
# •	On the next several lines, you will receive integers - the indexes.
# Output
# •	When the program ends, you must print the summed value of all removed elements.
# Constrains
# •	The input data will consist only of valid integers in the range [-2.147.483.648…2.147.483.647]

def remove_number(numbers_list, index_number, removed):
    numbers_list.pop(index_number)
    for index_number in range(len(numbers_list)):
        if numbers_list[index_number] <= removed:
            numbers_list[index_number] += removed
        else:
            numbers[index_number] -= removed


numbers = input()
numbers = list(map(int, numbers.split()))
sum_removed_elements = 0

while len(numbers) > 0:
    index = int(input())
    if index < 0:
        index = 0
        removed_number = numbers[0]
        remove_number(numbers, index, removed_number)
        numbers.insert(0, numbers[-1])

    elif index >= len(numbers):
        index = -1
        removed_number = numbers[-1]
        remove_number(numbers, index, removed_number)
        numbers.append(numbers[0])


    else:
        removed_number = numbers[index]
        remove_number(numbers, index, removed_number)

    sum_removed_elements += removed_number
print(sum_removed_elements)
