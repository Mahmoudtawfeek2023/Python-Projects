# 5.6.10.1.1 Build your Point Dictionary

# Define the letters and points lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create the letter_to_points dictionary using a list comprehension and zip
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add a key-value pair for blank tiles
letter_to_points[" "] = 0


# 5.6.10.1.2 Score a Word

# Define the score_word function
def score_word(word):
    # Initialize the point_total variable
    point_total = 0
    # Iterate through each letter in the word
    for letter in word:
        # Add the point value of the letter to the point_total variable
        point_total += letter_to_points.get(letter.upper(), 0)
    # Return the total points for the word
    return point_total

# Test the score_word function with the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)


# 5.6.10.1.3 Score a Game

# Create the player_to_words dictionary
player_to_words = {
    "Player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexicon": ["ERASER", "BELLY", "HUSKY"],
    "ProfReader": ["ZAP", "COMA", "PERIOD"]
}

# Create the player_to_points dictionary
player_to_points = {}

# Iterate through each player and their list of words in player_to_words
for player, words in player_to_words.items():
    # Initialize the player_points variable
    player_points = 0
    # Iterate through each word in the player's list of words
    for word in words:
        # Add the points for the word to the player's total points
        player_points += score_word(word)
    # Add the player and their total points to the player_to_points dictionary
    player_to_points[player] = player_points

# Print the current standings for the game
print(player_to_points)


# 5.6.10.1.4 Ideas for Further Practice!

# Define the update_point_totals function
def update_point_totals(player, word):
    # Add the word to the player's list of words
    player_to_words[player].append(word)
    # Calculate the player's total points
    player_points = sum(score_word(word) for word in player_to_words[player])
    # Update the player's total points in the player_to_points dictionary
    player_to_points[player] = player_points

# Define the play_word function
def play_word(player, word):
    # Update the player's list of words and total points
    update_point_totals(player, word)

# Test the updated functions by playing a word for Player1
play_word("Player1", "PYTHON")
print(player_to_words)
print(player_to_points)