from time import sleep
from paths import next_room
from game_mechanics import game_start, player_stats




def main():
    player = game_start()
    while player_stats["cur_hp"] > 0:
        next_room()



    

main()    
