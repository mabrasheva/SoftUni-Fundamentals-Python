# Create a class Weapon. The __init__ method should receive a number of bullets (integer).
# Create an attribute called bullets to store that number.
# The class should also have the following methods:
# •	shoot()
# o	If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
# o	If there are no bullets left, return: "no bullets left"
# •	__repr__()
# o	Returns "Remaining bullets: {amount_of_bullets}"

class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

# Tests:
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
