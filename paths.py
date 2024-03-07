# Rooms
import random

room_types = ["monster", "monster_elite", "merchant", "sacrafice", "floor_item", "trial", "boss", "campfire", "loot"]

def monster_room():
    pass
    # encounter a random enemy, win for a reward

def monster_elite_room():
    pass
    # encounter a random elite enemy, win for a greater reward

def merchant_room():
    pass
    # encounter a merchant that sells random items

def sacrafice_room():
    pass
    # sacrafice an item, gain a permanent buff depending on the item's gold cost

def floor_item_room():
    pass
    # choose between three items until you have 3 consumables

def trial_room(player_gold, player_attack, player_health):
    # if the player completes a trial, gain a buff
    trial_list = ["wealth", "vitality"]
    trial_type = random.choice(trial_list)

    # Trial of Wealth: have a certain amount of gold
    if trial_type == "wealth":
        print("The ghost of a long-dead merchant floats before you \"Traveler,\" he says, \"I offer the trial of wealth, carry 55 gold and recieve my boon.\"")
        input("Press any key to commence the trial of wealth")
        if player_gold >= 55:
            print("The merchant nods, \"You have passed my test, you may receive my boon. The blessing of life\"")
            print("MAX HP INCREASED")
            player_hp_bonus += 15
        else:
            print("The merchant frowns, \"You do not have enough gold, you cannot receive my boon.\"")
    
    # Trial of Vitality: have a certain amount of health
    if trial_type == "vitality":
        print("The ghost of a slain knight floats before you \"Traveler,\" he says, \"I offer the trial of vitality, possess 50 max health and recieve my boon.\"")
        input("Press any key to commence the trial of vitality")
        if player_health >= 50:
            print("\"You have passed my test, traveler.\" The knight bows his head, \"With the boon of strength, your blow shall strike true. May you succeed where I have failed, slay that monster.\"")
            print("DAMAGE INCREASED")
            player_attack_bonus += 5
        else:
            print("\"I apologize,\" the knight says, \"you lack the endurance to receive my blessing.\"")

def boss_room():
    pass
    # encounter the biome's boss.

def campfire_room():
    pass
    # restore health and mana
    # next room after a boss is always a campfire

def loot_room():
    pass
    # gain three random items, can be main_hand, off_hand, armor, or consumable

def room_transition():
    pass