# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one
# with space available.
# Input
# •	On the first line, you will receive how many people are waiting to get on the lift
# •	On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue, you should print on
# the console the final state of the lift's wagons separated by " " and one of the following messages:
# •	If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# •	If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# •	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

people = int(input())
wagons = input().split()
wagons = list(map(int, wagons))
people_left = people
wagon_capacity = 4
not_enough_space = False
the_lift_has_empty_spots = False

for index in range(len(wagons)):
    people_in_wagon = wagons[index]
    if people_in_wagon > wagon_capacity:
        continue
    else:
        wagon_empty_spots = wagon_capacity - people_in_wagon
        if people_left < wagon_empty_spots:
            wagons[index] += people_left
            if wagons[index] < wagon_capacity:
                the_lift_has_empty_spots = True
            people_left -= wagon_empty_spots
            break
        else:
            wagons[index] = wagon_capacity
            people_left -= wagon_empty_spots

if people_left > 0:
    not_enough_space = True

if the_lift_has_empty_spots:
    print("The lift has empty spots!")
if not_enough_space:
    print(f"There isn't enough space! {people_left} people in a queue!")
print(*wagons, sep=" ")
