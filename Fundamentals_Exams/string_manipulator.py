def translate(text: str, old_character: str, new_character: str):
    result = text.replace(old_character, new_character)
    print(result)
    return result


def includes(text: str, searched_string: str):
    if searched_string in text:
        print("True")
    else:
        print("False")


def start(text: str, searched_string: str):
    if text.startswith(searched_string):
        print("True")
    else:
        print("False")


def lowercase(text: str):
    result = text.lower()
    print(result)
    return result


def find_index(text: str, searched_character: str):
    index = text.rfind(searched_character)
    print(index)


def remove_func(text: str, start_index: int, number: int):
    result = text[:start_index] + text[start_index + number:]
    print(result)
    return result


input_string = input()
result_string = input_string

command = input()

while command != "End":
    command = command.split()
    action = command[0]
    if action == "Translate":
        character, replacement = command[1], command[2]
        result_string = translate(result_string, character, replacement)
    elif action == "Includes":
        substring = command[1]
        includes(result_string, substring)
    elif action == "Start":
        substring = command[1]
        start(result_string, substring)
    elif action == "Lowercase":
        result_string = lowercase(result_string)
    elif action == "FindIndex":
        character = command[1]
        find_index(result_string, character)
    elif action == "Remove":
        start, count = int(command[1]), int(command[2])
        result_string = remove_func(result_string, start, count)

    command = input()
