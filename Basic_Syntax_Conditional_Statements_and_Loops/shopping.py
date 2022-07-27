budget = int(input())

price = input()
budget_left = budget

while price != "End":
    price = int(price)

    if budget_left < price:
        print("You went in overdraft!")
        break

    budget_left -= price
    price = input()


else:
    print("You bought everything needed.")
