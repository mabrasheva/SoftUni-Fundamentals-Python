# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills.
# You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the
# messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case-insensitive and remove the count
# from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier
# count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# •	The first line holds n – the number of messages– integer in range [1…100];
# •	On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.


import re

pattern_star_letters = r"[star]"
pattern_message = r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([A|D])![^@\-!:>]*->(\d+)"

attacked_planets = []
destroyed_planets = []

count = int(input())
for line in range(count):
    message = input()
    key = re.findall(pattern_star_letters, message, flags=re.IGNORECASE)
    key_number = len(key)
    decrypted_message = [chr(ord(letter) - key_number) for letter in message]
    decrypted_message = "".join(decrypted_message)
    valid_message = re.search(pattern_message, decrypted_message)
    if valid_message:
        planet_name, population, attack_type, soldier_count = valid_message.groups()
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
