from time import sleep
import random

player_stats = {"atk":0, "max_hp":0, "cur_hp":0, "max_mana":0, "cur_mana":0, "gold": 0}
inventory = {"main_hand": [],
"off_hand": [],
"armor": [],
"consumables": []}



def main():
    while player_stats["cur_hp"] > 0:
        pass
    game_over() # show game over

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
    print("You stumble upon an old man.")
    player_name = input('"What is your name young traveler?"\n--')
    print(f'"{player_name}"')
    sleep(1)
    print('"That is a wonderful name."')
    print(f'"This is a treacherous path, {player_name}"')
    return player_name


def show_inventory():
    print(f"""Main Hand: {inventory['main_hand']}
    Off Hand: {inventory['off_hand']}
    Armor: {inventory['armor']}
    Consumables: {inventory['consumables']}
    Money: {player_stats['gold']}""")



def fight(enemy):
    print(f"You encounter {enemy}")
    turn_counter = 0
    while enemy["hp"] > 0 and player_stats["atk"] > 0:
        if 0 % 2 == 0: # Players turn
            player_choice = input(f"What will {player_name} \nAttack \nMagic \nItems \nDefend \n--").lower()
            if player_choice == "attack":
                print(f"{player_name} uses his weapon")
                print(f"{enemy} loses {player_stats['atk']} health")
            elif player_choice == "magic":
                if spellbook in inventory["off_hand"]:
                    pass
            elif player_choice == "items":
                show_inventory()
                print(f"What will {player_name} use?")
                item_choice = input("--").lower()
                if item in inventory["consumables"]:
                    
                    continue
                else:
                    print(f"You don't have {item_choice}")
                    continue
            elif player_choice == "defend":
                enemy[atk] = enemy[atk] * .80
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
show_inventory()
main()    
