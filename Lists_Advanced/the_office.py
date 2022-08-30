# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"


happiness_list = list(map(int, input().split()))
factor = int(input())
happiness_list = [number * factor for number in happiness_list]
average_happiness = sum(happiness_list) / len(happiness_list)


def happy_employees(happiness):
    if happiness >= average_happiness:
        return True
    return False


# happy_employees_list = [happy_employees(employee) for employee in happiness_list]  # returns a list of [True, False]
# happy_employees_count = happy_employees_list.count(True)  # calculates the count of happy employees.

happy_employees_list = list(filter(happy_employees, happiness_list))  # returns a list of the happy employees.

if len(happy_employees_list) >= len(happiness_list) / 2:
    print(f"Score: {len(happy_employees_list)}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees_list)}/{len(happiness_list)}. Employees are not happy!")
