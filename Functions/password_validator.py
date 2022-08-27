# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def password_validator(input_string):
    password_is_valid = True

    # •	It should be 6 - 10 (inclusive) characters long
    if not 6 <= len(input_string) <= 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    # •	It should consist only of letters and digits
    if not input_string.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False

    # •	It should have at least 2 digits
    counter_digits = 0
    for symbol in input_string:
        if symbol.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    if password_is_valid:
        print("Password is valid")


input_password = input()

password_validator(input_password)
