# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

def search_contact(contact_name, phonebook):
    if contact_name in phonebook:
        return f"{contact_name} -> {phonebook[contact_name]}"
    return f"Contact {contact_name} does not exist."


contact_dict = {}
input_contact = input()
while "-" in input_contact:
    name, phone_number = input_contact.split("-")
    contact_dict[name] = phone_number

    input_contact = input()
count = int(input_contact)
for searched_contact in range(count):
    searched_contact_name = input()
    print(search_contact(searched_contact_name, contact_dict))
