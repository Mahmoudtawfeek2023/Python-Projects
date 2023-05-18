def unique_english_letters(phrase, letters):
    # Set to keep track of unique letters
    unique_letters = set()
    # Loop through every letter in the alphabet
    for letter in letters:
        # If the current letter is found in the input phrase, add it to the set of unique letters
        if letter in phrase:
            unique_letters.add(letter)
    # Return the count of unique letters and the set of unique letters
    return len(unique_letters), unique_letters

# Prompt user for input
phrase = input("Enter a phrase to count unique English letters: ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
unique_count, unique_letters = unique_english_letters(phrase, letters)
print(f"Number of unique English letters in '{phrase}': {unique_count}")
print("Unique letters:", ", ".join(unique_letters))