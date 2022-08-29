# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon.
# There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

wagons_count = int(input())
wagons_list = [0] * wagons_count

command = input()

while command != "End":

    command = command.split()

    if command[0] == "add":  # you should add the number of people in the last wagon
        people_add_last_wagon = int(command[1])
        wagons_list[-1] += people_add_last_wagon

    elif command[0] == "insert":  # you should add the number of people at the given wagon
        wagon_index = int(command[1])
        people_insert_index_wagon = int(command[2])
        wagons_list[wagon_index] += people_insert_index_wagon

    elif command[0] == "leave":  # you should remove the number of people from the wagon.
        # There will be no case in which the people will be more than the count in the wagon.
        wagon_index = int(command[1])
        people_remove_index_wagon = int(command[2])
        wagons_list[wagon_index] -= people_remove_index_wagon

    command = input()

print(wagons_list)
