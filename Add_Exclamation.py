def add_exclamation():
    """
    Prompts the user to input strings and adds exclamation points to the end of each string until it is 20 characters long.
    
    Returns:
    A list of strings containing the original strings with exclamation points appended to the end if the length is less than 20, or the original strings if the length is already at least 20 characters.
    """
    inputs = []
    while True:
        word = input("Enter a string: ")
        inputs.append(word)
        while len(word) < 20:
            word += "!"
        print(f"Modified string: {word}")
        more_inputs = input("Do you want to add more inputs? (y/n) ")
        if more_inputs.lower() != "y":
            break
    return inputs

# Call the function to test it
result = add_exclamation()
print(result)