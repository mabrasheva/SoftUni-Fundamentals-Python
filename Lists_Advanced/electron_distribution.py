# You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of
# electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more
# electrons left. The rules for electron distribution are as follows:
# •	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
# For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# •	You should start filling the shells from the first one at the first position.
# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell
# and so on.
# In the end, print a list with the filled shells.

def electrons_per_shell(shell_number):
    return 2 * (shell_number ** 2)


def shells(electrons_count):
    electrons_list = []
    shell = 0
    while electrons_count > 0:
        shell += 1
        electrons_to_add = electrons_per_shell(shell)
        if electrons_to_add <= electrons_count:
            electrons_list.append(electrons_to_add)
            electrons_count -= electrons_to_add
        else:
            electrons_to_add = electrons_count
            electrons_list.append(electrons_to_add)
            electrons_count = 0
    return electrons_list


number_of_electrons = int(input())
print(shells(number_of_electrons))

# 1: 2 * (1 ** 2) = 2
# 2: 2 * (2 ** 2) = 8
# 3: 2 * (3 ** 2) = 18
# 4: 2 * (4 ** 2) = 32
