# Rooms
import main
import enemies
import items
import random

rooms_completed = 0

room_types = ["monster", "merchant", "treasure", "campfire" "trial", "boss"]


def monster_room():
    # encounter a random enemy, win for a reward
    monster = random.choice(enemies.enemies.keys())
    print(f"A {monster["name"]}, stands before you. It must be defeated if you wish to complete your quest")
    main.fight(monster)
    print(f"The{monster["name"]} has been defeated, you gained {monster["gold"]} gold!")
    main.playerstats["gold"] += monster["gold"]

def merchant_room():
    print("You come across a merchant resting by a fire. He turns to you and speaks")
    main.merchant()

def treasure_room():
    print("It appears some unfortunate would-be adventurer left some equipment here, perhaps you can find something of use...")

    item_count = random.randint(1,3)
    for item in range(item_count):
        found_item = random.choice(items.item_pool)
        print(f"You found a {found_item["name"]}, shall you take it? (overides current item)")
        while True:
            accept = input("Yes/No").lower()
            if accept == "yes":
                if found_item["type"] == "weapon":
                    print(f"You equipped the {found_item["name"]}")
                    main.inventory["main_hand"] = found_item
                    break
                elif found_item["type"] == "armor":
                    print(f"You equipped the {found_item["name"]}")
                    main.inventory["armor"] = found_item
                    break
                elif found_item["type"] == "shield" or found_item["type"] == "spellbook":
                    print(f"You equipped the {found_item["name"]}")
                    main.inventory["off_hand"] = found_item
                    break
                elif found_item["type"] == "consumable":
                    if len(main.inventory["consumables"]) < 3:
                        print(f"You put the {found_item["name"]} in your bag")
                        main.inventory["consumables"].append(found_item)
                        break
                    else:
                        print(f"As you shoved the {found_item["name"]} into your pack, you broke your {main.inventory["consumables"][0]["name"]}!")
                        main.inventory["consumeable"].pop(0)
                        main.inventory["consumables"].append(found_item)
                        break
            elif accept == "no":
                print(f"You left the {found_item["name"]} behind.")
                break
            else:
                print("Invalid input, try again")
            print("You found nothing else of value, and set off again towards the dragon's den.")
            

                    


def trial_room():
    # if the player completes a trial, gain a buff
    trial_list = ["wealth", "vitality"]
    trial_type = random.choice(trial_list)

    # Trial of Wealth: have a certain amount of gold
    if trial_type == "wealth":
        print("The ghost of a long-dead merchant floats before you \"Traveler,\" he says, \"I offer the trial of wealth, carry 55 gold and recieve my boon.\"")
        input("Press any key to commence the trial of wealth")
        if main.player_stats["gold"] >= 55:
            print("The merchant nods, \"You have passed my test, you may receive my boon. The blessing of life\"")
            print("MAX HP INCREASED")
            main.player_stats["max_hp"] += 15
        else:
            print("The merchant frowns, \"You do not have enough gold, you cannot receive my boon.\"")
    
    # Trial of Vitality: have a certain amount of health
    if trial_type == "vitality":
        print("The ghost of a slain knight floats before you \"Traveler,\" he says, \"I offer the trial of vitality, possess 50 max health and recieve my boon.\"")
        input("Press any key to commence the trial of vitality")
        if main.player_stats["max_hp"] >= 50:
            print("\"You have passed my test, traveler.\" The knight bows his head, \"With the boon of strength, your blow shall strike true. May you succeed where I have failed, slay that monster.\"")
            print("DAMAGE INCREASED")
            main.player_stats["atk_up"] += 5
        else:
            print("\"I apologize,\" the knight says, \"you lack the endurance to receive my blessing.\"")

def boss_room():
    pass
    # encounter the biome's boss.

def campfire_room():
    # restore health and mana
    print("You come across an abandoned campsite, this looks to be a safe place to rest and recover.")
    input("Press any key to continue")
    main.player_stats["cur_hp"] = main.player_stats["max_hp"]
    main.player_stats["cur_mana"] = main.player_stats["max_mana"]

room_pool = ["monster", "merchant", "treasure", "campfire"]

def next_room():
    if rooms_completed == 0:
        treasure_room()
    elif rooms_completed <= 9:
        room_option_1 = random.choice(list(room_pool.keys()))
        room_option_2 = random.choice(list(room_pool.keys()))
        print(f"Two roads lie before you, one the left path, you will find a {room_option_1}, on the right path you will find a {room_option_2}, which way do you go?")
        while True:
            which_way = input("left or right?")
            if which_way.lower() == "left":
                if room_option_1 == "monster":
                    monster_room()
                    break
                elif room_option_1 == "merchant":
                    merchant_room()
                    break
                elif room_option_1 == "treasure":
                    treasure_room()
                    break
                elif room_option_1 == "campfire":
                    campfire_room()
                    break
            elif which_way.lower() == "right":
                if room_option_2 == "monster":
                    monster_room()
                    break
                elif room_option_2 == "merchant":
                    merchant_room()
                    break
                elif room_option_2 == "treasure":
                    treasure_room()
                    break
                elif room_option_2 == "campfire":
                    campfire_room()
                    break
            else:
                print(f"{which_way} is not left or right, try again.")
    elif rooms_completed == 10:
        trial_room()
    elif rooms_completed == 11:
        boss_room()

    rooms_completed += 1