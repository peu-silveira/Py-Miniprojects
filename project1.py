import random # random module allows to generate random numbers

def roll(): # creating a roll function
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value) # using the method .randint it chooses a random int within a max and a min int

    return roll # this return will give whoever called the function, this random value

# Setting up the game

# 1) Asking how many players will participate

while True: # this loop is to continue to ask for a valid number of players (2 to 4)
    players = input("Enter the number of players ( 2 - 4 ): ")
    if players.isdigit(): #method .isdigit will tell if its a number or not
        players = int(players) # also transforming the response into a integer, to make sure lol
        if 2 <= players <= 4:
            break # if the number given is valid, its gona break out of the while 
        else:
            print("Must be between 2 - 4 players.")
    else: 
        print("Invalid, try again.")



# 2) Simulate each players turn, asking if they wanna roll the dice, and start calculating the score

max_score = 50 # limiting the points cap
player_scores = [0 for _ in range(players)] # its a list that puts a 0 inside the list for every single player that we have
# we are now able to store the scores inside this array

while max(player_scores) < max_score: # this loop means keep going until reach the max_score

    for player_idx in range(players): # this will loop into the different players 
        print("\nPlayer number", player_idx  + 1, "turn has just started!") # \n adds a line break
        print("Your total socre is:", player_scores[player_idx], "\n")
        current_score = 0

        while True: 
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y": # method .lower is to make sure it recognizes Y or y
                break
    
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!") # heres where the players turn ends
                current_score = 0 # and the score turns into 0
                break
            else:
               current_score += value
               print("You rolled a ", value)

            print("Your current score is: ", current_score)
        
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

# The game ends when one of the player hits the score of 50
# even after hitting 50, the remain players still have a last chance of rolling the dice to get the 50 points
    
