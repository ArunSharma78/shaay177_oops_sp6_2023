from Player import Player

class CommandLineInterface:

    def __init__(self):
        pass

    def display_greeting(self):
        print(f"Welcome to All-That-Dice!")
        print(f"Developed by Arun Sharma")
        print(f"COMP 1048 Object-Oriented Programming")

    def display_main_menu(self):
        print(f"\nWhat would you like to do?")
        print(f" (r) register a new player")
        print(f" (s) show the leader board")
        print(f" (p) play a game")
        print(f" (q) quit")

    def register_new_player(self):
        print(f"{Player.check_player_exist('test')}")


game1 = CommandLineInterface()
player1 = Player()
game1.display_greeting()

user_input = input(game1.display_main_menu())
while user_input.lower() != "q":
    if user_input.lower() == "r":
        playerToAdd = input("What is the name of the new player?\n>")
        if player1.add_player(playerToAdd) == True:
            print(f"Welcome, {playerToAdd}!")
        else:
            print("Sorry, the name is already taken.")

    else:
        print("exist from else")

    print(f"chips of the player Alan: {player1.chips('Alan')}")
    player1.update_chips("Alan", 90, "Add")
    print(f"chips of the player Alan: {player1.chips('Alan')}")
    user_input = input(game1.display_main_menu())











    