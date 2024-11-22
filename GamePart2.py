import random

print("Welcome to the Kingdom of Eldoria!")

print("The land has been plagued by darkness, and monsters roam free.")

print("You, a noble knight, are tasked with restoring peace to the realm.")

print("Gather gold, find weapons, and embark on dangerous quests to defeat the evil threatening the kingdom.")

# Gold or Health reaches 0?


def check_game_over():
    if health <= 0:
        print("Your health has dropped to zero. You have been defeated... Game Over!")
        return True
    elif gold <= 0:
        print("You've run out of gold and must return to the kingdom. Game Over!")
        return True
    return False

# Knight Health


health = 100

print("Your current health is:", health)

# Health Func


def change_health(amount):
    global health
    health += amount
    if health > 100:
        health = 100
        print("Your health is maxed out, go explore!")
    print("Your health is now:", health)

# Gold Func


def change_gold(amount):
    global gold
    gold += amount
    print("Your gold is now: ", gold)

# gold


gold = 50

print("You start with", gold, "gold pieces")

# Weapon

weapon = "Sword"

print("Your weapon of choice is a:", weapon)

# Adding an item


def add_item_to_inventory(item_name):
    # Example usage: add_item_to_inventory("Healing Potion")
    inventory.append(item_name)
    print("You found a", item_name + "!", items[item_name]['description'])


def show_inventory():
    # Check your inventory
    print("Your current inventory:")
    for item in inventory:
        print("-", item + ":", items[item]['description'])


def use_item(item_name):
    if items[item_name]["type"] == "potion":
        change_health(items[item_name]["effect"])
    elif items[item_name]["type"] == "treasure":
        change_gold(items[item_name]["effect"])
    inventory.remove(item_name)
    print("You used", item_name, "!")

# Inventory


inventory = []

print("Your inventory is currently empty:", inventory)

# Let's define some items:

items = {
    "Healing Potion": {"description": "A potion that restores your health.", "type": "potion", "effect": 20},
    "Gold Nugget": {"description": "A shiny nugget that increases your wealth.", "type": "treasure", "effect": 10}
}

# Name

player_name = input("What is your knight's name?")

print("Welcome, brave knight", player_name, "!")

is_fighting = False

while True:
    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Rest")
    print("3. Check Stats")
    print("4. Quit")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You venture into the wilderness...")
        encounter = random.choice(["enemy", "treasure", "nothing", "item"])
        if encounter == "enemy":
            print("An enemy appears! Prepare to fight!")
            print(
                "If you choose to fight, you may gain gold if you win, but lose health if you lose.")
            print(
                "If you choose to flee, you will avoid combat but lose 25 gold as the cost of retreat.")
            is_fighting = True
            while is_fighting:
                fight_choice = input(
                    "Do you want to fight (1), flee (2), or check inventory (3)?")
                if fight_choice == "1":
                    print("You chose to fight!")
                    fight_result = random.choice(["victory", "defeat"])
                    if fight_result == "victory":
                        print("You defeated the enemy and found 20 gold!")
                        change_gold(20)
                        is_fighting = False
                    else:
                        print("You were defeated and lost 15 health!")
                        is_fighting = False

                elif fight_choice == "2":
                    print(
                        "You chose to flee! You escaped but lost 25 gold in the process.")
                    change_gold(-25)
                    is_fighting = False

                elif fight_choice == "3":
                    show_inventory()
                    item_choice = input(
                        "Choose an item to use, or press Enter to return: ")
                    if item_choice in inventory:
                        use_item(item_choice)
                    else:
                        print("No item used.")
                else:
                    print("Invalid choice. You continue on your fight.")
        elif encounter == "treasure":
            print("You found a hidden treasure chest and gained 50 gold!")
            change_gold(50)
        elif encounter == "item":
            found_item = random.choice(list(items.keys()))
            add_item_to_inventory(found_item)
        else:
            print("Nothing happened on your journey this time.")
    elif choice == "2":
        print("You take a rest and regain health.")
        change_health(20)
    elif choice == "3":
        print("Checking your stats:")
        print("Health:", health)
        print("Gold:", gold)
        print("Weapon:", weapon)
        print("Inventory:", inventory)
    elif choice == "4":
        print("Goodbye, brave knight!")
        break
    else:
        print("Invalid choice, please choose again.")
    if check_game_over():
        break

print("Thanks for playing!")
