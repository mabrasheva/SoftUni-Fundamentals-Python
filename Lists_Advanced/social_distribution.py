# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and
# that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line,
# you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than
# the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print:
# "No equal distribution possible".

def equal_distribution(numbers_list, wealth_number):
    min_number = min(numbers_list)
    max_number = max(numbers_list)

    while wealth_number > min_number:
        min_number_index = numbers_list.index(min_number)
        max_number_index = numbers_list.index(max_number)

        diff = wealth_number - min_number
        numbers_list[min_number_index] += diff
        numbers_list[max_number_index] -= diff

        min_number = min(numbers_list)
        max_number = max(numbers_list)

    return numbers_list


population = input().split(", ")
population = list(map(int, population))
wealth = int(input())

if sum(population) < wealth * len(population):
    print("No equal distribution possible")
else:
    result = equal_distribution(population, wealth)
    print(result)

# Example:
# wealth = 5
# max = 75
# min = 2
# diff = wealth - min = 3
# min + diff
# max - diff
