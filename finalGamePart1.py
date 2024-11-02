import random

print("Welcome to the Kingdom of Eldoria!")

print("The land has been plagued by darkness, and monsters roam free.")

print("You, a noble knight, are tasked with restoring peace to the realm.")

print("Gather gold, find weapons, and embark on dangerous quests to defeat the evil threatening the kingdom.")

# Knight Health

health = 100

print("Your current health is:", health)

# gold

gold = 50

print("You start with", gold, "gold pieces")

# Weapon 

weapon = "Sword"

print("Your weapon of choice is a:", weapon)

# Inventory

inventory = []

print("Your inventory is currently empty:", inventory)

# Name

player_name = input("What is your knight's name?")

print("Welcome, brave knight", player_name , "!")

while True:
    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Rest")
    print("3. Check Stats")
    print("4. Quit")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You venture into the wilderness...")
        encounter = random.choice(["enemy", "treasure", "nothing"])
        if encounter == "enemy":
            print("An enemy appears! Prepare to fight!")
            print("If you choose to fight, you may gain gold if you win, but lose health if you lose.")
            print("If you choose to flee, you will avoid combat but lose 25 gold as the cost of retreat.")
            fight_choice = input("Do you want to fight (1) or flee (2)? ")
            if fight_choice == "1":
                print("You chose to fight!")
                fight_result = random.choice(["victory", "defeat"])

                if fight_result == "victory":
                    print("You defeated the enemy and found 20 gold!")
                    gold += 20
                else:
                    print("You were defeated and lost 15 health!")
                    health -= 15
            elif fight_choice == "2":
                print("You chose to flee! You escaped but lost 25 gold in the process.")
                gold -= 25
            else:
                print("Invalid choice. You continue on your fight.")
        elif encounter == "treasure":
            print("You found a hidden treasure chest and gained 50 gold!")
            gold += 50
        else:
            print("Nothing happened on your journey this time.")
    elif choice == "2":
        print("You take a rest and regain health.")
        health += 20
        print("Current health:", health)
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

        
        
        
        
        
        














