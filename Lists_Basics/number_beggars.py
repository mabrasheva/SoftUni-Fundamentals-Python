# You will receive 2 lines of input.
# On the first line, you will receive a single string of integers, separated by a comma and a space ", ".
# On the second line, you will receive a count of beggars.
# Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns,
# from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5],
# the second one collects [2, 4]. The same list with 3 beggars would produce a better outcome for the second beggar:
# 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not
# necessarily a multiple of n. The list length could be even shorter - i.e., the last beggars will take nothing (0).

sum_list_of_strings = input().split(", ")
beggars_count = int(input())
sum_list_of_integers = []
final_list_beggars = []
for index in range(len(sum_list_of_strings)):
    sum_list_of_integers.append(int(sum_list_of_strings[index]))

for beggar in range(beggars_count):
    beggar_money = 0
    for index in range(beggar, len(sum_list_of_integers), beggars_count):
        beggar_money += sum_list_of_integers[index]
    final_list_beggars.append(beggar_money)
    beggar += 1
print(final_list_beggars)
