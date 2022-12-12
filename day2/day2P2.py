
# Scores
ROCK = 1
PAPER = 2
SCISSORS = 3
LOST = 0
DRAW = 3
WIN = 6

# Player 1 Encryptions
player_1_dict = {
    "A" : ROCK,
    "B" : PAPER,
    "C" : SCISSORS
}

# Player 2 Encryptions
player_2_dict = {
    "X" : LOST,
    "Y" : DRAW,
    "Z" : WIN
}

# Decodes each player's input to be RPS.
def decodePlayerInput(input, player_id):
    if not player_id:
        return player_1_dict[input]
    else:
        return player_2_dict[input]

# Decodes our player's input to be the status of the game.
def decodeResultStatus(player_2):
    if player_2 == DRAW:
        player_2 = player_1
    elif player_2 == WIN:
        if player_1 == SCISSORS:
            player_2 = ROCK
        elif player_1 == PAPER:
            player_2 = SCISSORS
        else:
            player_2 = PAPER
    else:
        if player_1 == ROCK:
            player_2 = SCISSORS
        elif player_1 == SCISSORS:
            player_2 = PAPER
        else:
            player_2 = ROCK

    return player_2

# Play the game of Rock Paper Scissors.
def playGame(player_1, player_2):
    if player_1 == player_2:
        return DRAW + 1

    if ((player_1 == ROCK and player_2 == SCISSORS) or
        (player_1 == SCISSORS and player_2 == PAPER) or
        (player_1 == PAPER and player_2 == ROCK)):
        return player_1
    elif ((player_1 == SCISSORS and player_2 == ROCK) or 
        (player_1 == PAPER and player_2 == SCISSORS) or
        (player_1 == ROCK and player_2 == PAPER)):
        return player_2

input = open("input.txt")

lines = input.readlines()

player_1_score = 0
player_2_score = 0

for line in lines:
    players_input = line.split(" ")

    # Decodes each input.    
    player_1 = decodePlayerInput(players_input[0].strip(), 0)
    player_2 = decodePlayerInput(players_input[1].strip(), 1)

    # Decodes our player to be the status of the game.
    player_2 = decodeResultStatus(player_2)
    
    # Play the game.
    result = playGame(player_1, player_2)

    if result == DRAW + 1:
        player_1_score += player_1 + DRAW
        player_2_score += player_2 + DRAW
    elif result == player_1:
        player_1_score += player_1 + WIN
        player_2_score += player_2 + LOST
    else:
        player_1_score += player_1 + LOST
        player_2_score += player_2 + WIN


print("My Score: " + str(player_2_score))
