from time import sleep
import random

player_stats = {"atk":0, "max_hp":0, "cur_hp":0, "max_mana":0, "cur_mana":0}


def main():
    pass

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
    print(f"{player_name}")
    sleep(1)
    print('"That is a wonderful name."')
    print(f'"This is a treacherous path, {player_name}"')
    return player_name


# player_name = game_start()

def inventory():
    main_hand = []
    off_hand = []
    armor = []
    consumables = []



def fight(enemy):
    print(f"You encounter {enemy}")
    while enemy["hp"] > 0:
        player_choice = input(f"What will {player_name} \nAttack \nMagic \nItems \nDefend \n--").lower()
        if player_choice == "attack":
            print(f"{player_name} uses his weapon")
            print(f"{enemy} loses {player_stats['atk']} health")
        elif player_choice == "magic":
            if spellbook:
                pass
        elif player_choice == "items":
            pass
        elif player_choice == "defend":
            enemy[atk] = enemy[atk] * .80
        else:
            print("Not possible")


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



# main()    

game_over()
