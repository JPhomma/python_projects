import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit() and 5 > int(players) > 0:
        players = int(players)
        break
    else:
        print("Invalid try again. Please enter a number between 1-4")
        
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) <= max_score:
    end_turn_value = 1
    current_index = 0
    for player in player_scores:
        current_index = current_index + 1
        playerIndex = player_scores.index(player)
        if current_index == playerIndex:
            print("\nPlayer number", playerIndex + 1, "'s turn has just started!\n")
        current_score = player_scores[playerIndex] if player_scores[playerIndex] > 0 else 0
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() == 'y':
            value = roll()
            print("You rolled a:" + str(value))
            player_scores[playerIndex] = current_score + value
            if end_turn_value == value:
                print("Next player's turn")
                print("Current scores:", player_scores)
                print("\nPlayer number", playerIndex + 1, "'s turn has just started!\n")
                break
        else:
            break
        print("Current scores:", player_scores)
            