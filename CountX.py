# Define the count_char_x function
def count_char_x(word, x):
    # Counter for occurrences of character x
    count = 0
    # Loop through every character in the string
    for character in word:
        # If the current character is equal to character x, increase the counter
        if character == x:
            count += 1
    # Return the count of occurrences of character x
    return count

# Loop to ask for input and count characters
while True:
    # Prompt user for input string and validate
    while True:
        word = input("Enter a string with no spaces: ")
        if ' ' in word:
            print("Error: String must not contain spaces")
        else:
            break
    # Loop to ask for characters to count
    while True:
        x = input("Enter a character to count in the string (press Enter to quit): ")
        if x == '':
            break
        else:
            count = count_char_x(word, x)
            print(f"The character '{x}' appears {count} times in '{word}'")
    # Ask user if they want to input another string
    another = input("Do you want to count characters in another string? (y/n): ")
    if another.lower() != 'y':
        break