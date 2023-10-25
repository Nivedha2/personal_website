import pandas as pd

#choice_one = input("Choose X or O for player one: ")
#choice_two = input("Choose X or O for player two: ")

choice = input("Do you want to start game? Enter 1 to start game. 2 to play again. 0 to quit: ")

blank_table = [["_", "_", "_"],
               ["_", "_", "_"],
                ["_", "_", "_",]]

start_tab = pd.DataFrame(blank_table)

choice_one = int(input("Where do you want to place your letter? (Row,Column)"))

print(start_tab)


