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

def trial_room():
    pass
    # if the player completes a trial, gain a buff
    trial_types = ["wealth", "ring", "might", "vitality"]
    # Trial of Wealth: have a certain amount of gold
    # Trial of the Ring: have a ring in your inventory
    # Trial of Might: have a certain amount of attack power
    # Trial of Vitality: have a certain amount of health

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