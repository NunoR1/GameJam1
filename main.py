from time import sleep
import random
import items

player_stats = {"atk": 0, "max_hp": 0, "cur_hp": 0, "max_mana": 0, "cur_mana": 0, "gold": 0}
inventory = {"main_hand": [],
             "off_hand": [],
             "armor": [],
             "consumables": []}


def main():
    while player_stats["cur_hp"] > 0:
        pass
    game_over()  # show game over


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


def merchant():
    for let in "\nWelcome tired traveler...":
        print(let, end='')
        sleep(0.05)
    sleep(1)
    for let in "\nTake a look around and see if you fancy an item...":
        print(let, end='')
        sleep(0.05)
    sleep(1)

    print("\n\nSHOP ITEMS")
    print("----------")

    current_items = []
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)
    random_item = random.choice(list(items.item_pool))
    current_items.append(random_item)

    item_num = 0
    for item in current_items:
        item_num += 1
        print(f"{item_num}.", item["name"], "-", item["gold_value"], "Gold")

    print("----------")

    while True:
        purchase = input("Which # item would you like to buy? (or e to exit) \n--")
        if purchase.lower() == 'e':
            item_purchased = False
            break
        else:
            try:
                purchase_num = int(purchase) - 1
                if 0 <= purchase_num < len(current_items):
                    purchased_item = current_items[purchase_num]
                    if player_stats['gold'] >= purchased_item['gold_value']:
                        player_stats['gold'] -= purchased_item['gold_value']
                        if purchased_item['type'] == 'weapon':
                            if len(inventory['main_hand']) < 1:
                                inventory['main_hand'].append(purchased_item)
                                item_purchased = True
                                print(f"Fine choice traveller... You have purchased {purchased_item['name']} for {purchased_item['gold_value']}")
                            else:
                                item_replacement = input(f"It seems that you already have {inventory['main_hand'][0]['name']} equipped. Do you want to replace it with {purchased_item['name']}? (y/n)")
                                if item_replacement.lower() == 'y':
                                    inventory['main_hand'][0] = purchased_item
                                    item_purchased = True
                                    print(f"You have replaced your existing weapon with {purchased_item['name']} for {purchased_item['gold_value']} Gold.")
                                else:
                                    print(f"You decided to keep {inventory['main_hand'][0]['name']} in your weapon slot.")
                        elif purchased_item['type'] == 'armor':
                            if len(inventory['armor']) < 1:
                                inventory['armor'].append(purchased_item)
                                item_purchased = True
                                print(
                                    f"Fine choice traveller... You have purchased {purchased_item['name']} for {purchased_item['gold_value']}")
                            else:
                                item_replacement = input(
                                    f"It seems that you already have {inventory['armor'][0]['name']} equipped. Do you want to replace it with {purchased_item['name']}? (y/n)")
                                if item_replacement.lower() == 'y':
                                    inventory['armor'][0] = purchased_item
                                    item_purchased = True
                                    print(
                                        f"You have replaced your existing armor with {purchased_item['name']} for {purchased_item['gold_value']} Gold.")
                                else:
                                    print(f"You decided to keep {inventory['armor'][0]['name']} in your armor slot.")
                        elif purchased_item['type'] == 'shield' or purchased_item['type'] == 'spellbook':
                            if len(inventory['off_hand']) < 1:
                                inventory['off_hand'].append(purchased_item)
                                item_purchased = True
                                print(f"Fine choice traveller... You have purchased {purchased_item['name']} for {purchased_item['gold_value']}")
                            else:
                                item_replacement = input(
                                    f"It seems that you already have {inventory['off_hand'][0]['name']} equipped. Do you want to replace it with {purchased_item['name']}? (y/n)")
                                if item_replacement.lower() == 'y':
                                    inventory['off_hand'][0] = purchased_item
                                    item_purchased = True
                                    print( f"You have replaced your existing off hand with {purchased_item['name']} for {purchased_item['gold_value']} Gold.")
                                else:
                                    print(f"You decided to keep {inventory['off_hand'][0]['name']} in your Off Hand.")
                    else:
                        print("You don't have enough Gold to purchase that item.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Invalid input. Please enter a valid item number or 'e' to exit.")
    # if item_purchased:
    #     for let in "\nEnjoy your purchase traveler... wishing that your item serves you well.":
    #         print(let, end='')
    #         sleep(0.05)
    #     sleep(1)
    # elif not item_purchased:
    #     for let in "\nCome back anytime.":
    #         print(let, end='')
    #         sleep(0.05)
    #
    #     sleep(1)


def fight(enemy):
    print(f"You encounter {enemy}")
    turn_counter = 0
    while enemy["hp"] > 0 and player_stats["atk"] > 0:
        if 0 % 2 == 0:  # Players turn
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
        else:  # Enemy turn
            print(f"{enemy} attacks")
            hurt = enemy["damage"] * random.randint(0,
                                                    3)  # multiplies the damage value the enemy deals by a random value 0-3 so that it can miss, do a light, medium, or heavy
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
merchant()
