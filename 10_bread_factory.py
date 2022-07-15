input_string = input()
input_list = input_string.split("|")
energy = 100
coins = 100
is_bankrupt = False
for element in input_list:
    list_element = element.split('-')
    if list_element[0] == "rest":
        if energy == 100:
            energy_gain = 0
            print(f"You gained {energy_gain} energy.")
            print(f"Current energy: {energy}.")
            continue
        else:
            energy_gain = int(list_element[1])
            energy += energy_gain
            if energy > 100:
                energy_gain = int(list_element[1]) - (energy - 100)
                energy = 100
            print(f"You gained {energy_gain} energy.")
            print(f"Current energy: {energy}.")
            continue
    elif list_element[0] == "order":
        energy -= 30
        if energy > 0:
            coins_earned = int(list_element[1])
            coins += coins_earned
            print(f"You earned {coins_earned} coins.")
            continue
        else:
            energy += 80
            if energy > 100:
                energy = 100
            print(f"You had to rest!")
            continue
    else:
        coins_spent = int(list_element[1])
        coins -= coins_spent
        if coins >= 0:
            print(f"You bought {list_element[0]}.")
            continue
        else:
            is_bankrupt = True
            print(f"Closed! Cannot afford {list_element[0]}.")
            break
if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



