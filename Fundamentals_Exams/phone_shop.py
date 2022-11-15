def add(phone_to_add, phones_list):
    if phone_to_add not in phones_list:
        phones_list.append(phone_to_add)
    return phones_list


def remove(phone_to_remove, phones_list):
    if phone_to_remove in phones_list:
        phones_list.remove(phone_to_remove)
    return phones_list


def bonus(old, new, phones_list):
    if old in phones_list:
        phones_list.insert(phones_list.index(old) + 1, new)
    return phones_list


def last_phone(phone_to_go_last, phones_list):
    if phone_to_go_last in phones_list:
        phones_list.remove(phone_to_go_last)
        phones_list.append(phone_to_go_last)
    return phones_list


phones = input().split(", ")

command = input()
while command != "End":
    action, phone = command.split(" - ")
    if action == "Add":
        phones = add(phone, phones)
    elif action == "Remove":
        phones = remove(phone, phones)
    elif action == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        phones = bonus(old_phone, new_phone, phones)
    elif action == "Last":
        phones = last_phone(phone, phones)

    command = input()

print(*phones, sep=", ")
