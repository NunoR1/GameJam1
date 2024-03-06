from time import sleep

inventory = []


def main():
    game_start()


def game_start():

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



def inventory():
    pass

main()