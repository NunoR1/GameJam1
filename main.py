from time import sleep
import random
from items import weapons, offhand, armors, consumables
from paths import next_room

player_stats = {"atk":0, "max_hp":10, "cur_hp":10, "max_mana":20, "cur_mana":0, "gold": 0, "atk_up": 0}
inventory = {"main_hand": [weapons["Old Sword"]],
"off_hand": [offhand["Plank Shield"]],
"armor": [armors["Cloth Armor"]],
"consumables": []}



def main():
    while player_stats["cur_hp"] > 0:
        next_room()


def game_start():
    # Opening dialogue
    print("You are in a path in the woods.")
    sleep(1)
    print("The darkness of the forest looms around you.")
    sleep(1)
    print("You are on a quest to slay a dragon")
    sleep(1)
    print("The end of the path is nearing")
    sleep(1)
    print("You stumble upon a cabin")
    print("Within the cabin there is an old man.")
    player_name = input('"What is your name young traveler?"\n--')
    print(f'"{player_name}"')
    sleep(1)
    print('"That is a wonderful name."')
    sleep(1)
    print(f'"This is a treacherous path, {player_name}"')
    return player_name


def show_inventory():
    print(f"""Main Hand: {inventory['main_hand'["name"]]}
    Off Hand: {inventory['off_hand'["name"]]}
    Armor: {inventory['armor'["name"]]}
    Consumables: {inventory['consumables'["name"]]}
    Money: {player_stats['gold'["name"]]}""")



def fight(enemy):
    turn_counter = 0
    while enemy["health"] > 0 and player_stats["hp"] > 0:
        
        if turn_counter % 2 == 0: # Players turn
            player_choice = input(f"What will {player_name} \nAttack \nMagic \nItems \nDefend \n--").lower()
            
            if player_choice == "attack":
                print(f"{player_name} uses his weapon")
                print(f"{enemy} loses {player_stats['atk']} health")
            
            elif player_choice == "magic":
                if "Spellbook" in inventory["off_hand"]:
                    print("Blast: 3 Mana \nHeal: 4 Mana")
                    the_magics = input("--")
                    if the_magics == "Blast" and player_stats["cur_mana"] >= 3:
                        enemy["health"] -= offhand["Spellbook"["offense_spell_damage"]] * inventory["main_hand"["magic_mod"]]
                        player_stats["cur_mana"] -= 3
                    
                    elif the_magics == "Heal" and player_stats["cur_mana"] >= 4:
                        player_stats["cur_hp"] += offhand["Spellbook"["defense_spell_healing"]] * inventory["main_hand"["magic_mod"]]
                        player_stats["cur_mana"] -= 4

                    else:
                        print("You don't have enough mana")

                else:
                    print("You have no spellbooks")
                    continue
            
            elif player_choice == "items":
                show_inventory()
                print(f"What will {player_name} use?")
                item_choice = input("--").capitalize()  # what the player wants
                if item_choice in inventory["consumables"]:
                    print(f"{player_name} uses {item_choice}")
                    
                    if item_choice == "Healing Potion":
                        player_stats["cur_hp"] += consumables["Healing Potion"["strength"]]
                        if player_stats["cur_hp"] > player_stats["max_hp"]:  # Make sure that there is a mana cap
                            player_stats["cur_hp"] = player_stats["max_hp"]
                    
                    elif item_choice == "Mana Potion":
                        player_stats["cur_mana"] += consumables["Mana Potion"["strength"]]
                        if player_stats["cur_mana"] > player_stats["max_mana"]:  # Make sure that there is a mana cap
                            player_stats["cur_mana"] = player_stats["max_mana"]
                    
                    elif item_choice == "Wand of Lightning":
                        enemy["health"] -= consumables["Lightning Wand"["strength"]] * inventory["main_hand"["magic_mod"]]
                    
                    elif item_choice == "Crossbow":
                        enemy["health"] -= consumables["Crossbow"["strength"]] * inventory["main_hand"["magic_mod"]]
                    continue
                
                else:
                    print(f"You don't have {item_choice}")
                    continue
            
            else:
                print("Not possible")
        
        
        else: # Enemy turn
            print(f"{enemy} attacks")
            hurt = enemy["damage"] * random.randint(0,3)  # multiplies the damage value the enemy deals by a random value 0-3 so that it can miss, do a light, medium, or heavy
            if hurt != 0:
                print(f"{enemy} dealt {hurt} damage")
                player_stats["cur_hp"] - hurt
            else:
                print(f"{enemy} missed")
    
        turn_counter += 1
    if enemy["health"] <= 0:
        print(f"{player_name} has turned out victorious")
    else:
        game_over()
    

def game_over():
    print("""                                                                                                    
                                        %%###########                                               
                                     %%#########%%###%                                              
                                  %%%%%%%%%%%%#########%                                            
                               %%%%%%%%%#*++*#####%%%###%                                           
                             %%%%%%%%%%#*+++==+++#%%%%%%%%                                    ++    
                            %%%%%%%%%%%*+**+=====+#%%%%%%%                         %   +===+++====+ 
                            %%%%%#%%%%%%*+++=====+#%%%%%%%%%%###%%%###%####%%%#########=-----=+***+ 
                                ##%%%%@%%*+++===*#%%%%%%%%%%###%#%%%%%%####%#%%%%######=----=+++    
                                   %%%@@@%#*++*%%%%%%%%%%%%%###%%%##%%#########%######              
                                     @@@@@@@@@@@%%%%%%%%%%%%%###%######%######%                     
     **++                             %%%%%%%%%%%%%%%%%%%%%%%%##########%%                          
    *+***++                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%##                                   
    +++**+==++++               %%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%###                                  
    ==+++========+++++++   %%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%###                                  
           ++============+*%%%%%%%%%%%%%%@%@%%%%%%%%%%%%%%%%%%####                                  
               ++===========*%%%%%%%%%%%%@%%@@%%%%%%%%%%%%%%%%####                                  
                    ++======*%%%%%%%%      %@@%%%%%%%%%%%%%%%#####                                  
                                             @%%%%%%%%%%%%%%%%####                                  
                                              %@%%%%%%%%%%%%%%%###                                  
                                              @@%%%%%%%###########                                  
                                              @@@%%%%%#####*+===**                                  
                                              @@@%%@@@@@%%%%%%%#+#                                  
                                  %%%%%%%%@@@@@@@%%%%%%%%%%%%%##%#                                  
                      %%%%%%%%%%%%%%%%%%%%%%@@@%@@@@@%%%%%%#%%####                                  
                    %%%%%%%%%%%%%%%%%%%%%%@@@@%%@@%%%%%%%#%%######                                  
                    %%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%%%%#####                                  
                    %%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%%%%%%####                                  
                    %%%%%%%%%%%%%%%%%%%%%@@@@@@@%%%%%%%%#########                                   
                      %%%%%%%%%%%@@@%%%%@@@@@@@%%##%#############                                   
                       %%%%%%%%%%%@        @%%%%%#######%%#####%                                    
                        %%%%%%%%%%@@         %%%#######%%#%###                                      
                          %%%%%%%%%@@       %%%%######%%####                                        
                           %%%%%%%@@@     @%%%######%####                                           
                            %%%%%%@@@@@   %%%%%####%####                                            
                             %%%%%%@@@@@ %%%%%#%%%#####                                             
                              %%%%%@@@%%%%####%%%#####                                              
                               %%%%%%%######%%%%%###                                                
                                %%%##%%%%%%%%%%###                                                  
                                 ##%%%%##%%%%%%%#                                                   
                                 **#*#%%%%%%%%%%#%                                                  
                                 +*#+*#%%%%%%%%%###                                                 
                                 +**++*#%%%%%%%%%####                                               
                                  #%%#*#%%%%%%%%%%%###                                              
                                  %%#*####%%%%%%%%%%###                                             
                                  ##*####% %%%%%%#######                                            
                                 %#*####     %%%#########                                           
                                  *####        %##########                                          
                                                %##########                                         
                                                 %%#########                                        
                                                   %#########% ##*#                                 
                                                    %########*##*=+                                 
                                                      #######*##*--+                                
                                                       ####***##+:--                                
                                                        *****###+:::                                
                                                       #*+*##*+--:::                                
                                                        ===++-++-::-                                
                                                          ++*=-++-:-                                
                                                           +**+=++--                                
                                                            *#####--                                
                                                            ######-=                                
                                                             %%###-+                                
                                                             %%##+-                                 
                                                             %###=+                                 
                                                              %#++                                  
                                                                                                    """)
    sleep(2)
    print("You have met a terrible fate.")
    restart = input("Restart?\nYes         No\n--").lower()
    if restart == "yes":
        main()
    else:
        pass


player_name = game_start()
main()    
