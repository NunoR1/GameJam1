# Rooms
import main
import enemies
import items
import random

rooms_completed = 0

room_types = ["monster", "merchant", "floor_item", "trial", "boss", "campfire",]

def monster_room():
    # encounter a random enemy, win for a reward
    monster = random.choice(enemies.enemies.keys())
    print(f"A {monster["name"]}, stands before you. It must be defeated if you wish to complete your quest")
    main.fight(monster)
    print(f"The{monster["name"]} has been defeated, you gained {monster["gold"]} gold!")
    main.playerstats["gold"] += monster["gold"]

def merchant_room():
    pass
    # encounter a merchant that sells random items

def floor_item_room():
    pass
    # choose between three items until you have 3 consumables

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
    player_stats["cur_hp"] = player_stats["max_hp"]
    player_stats["cur_mana"] = player_stats["max_mana"]

def room_transition():
    pass