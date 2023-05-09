import time

def check_for_name():
    """
    Prompts the user for their name and checks if the name contains a certain letter.
    
    Returns:
    A string containing a message about whether the name contains the letter "a".
    """
    name = input("What is your name? ")
    if "a" in name.lower():
        return f"Your name, {name}, contains the letter 'a'."
    else:
        return f"Your name, {name}, does not contain the letter 'a'."

def every_other_letter(word):
    """
    Returns every other letter of a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    A string containing every other letter of the input word.
    """
    return word[::2]

def reverse_string(word):
    """
    Reverses the characters of a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    A string containing the characters of the input word in reverse order.
    """
    return word[::-1]

def make_spoonerism():
    """
    Prompts the user for two words and creates a Spoonerism by switching the first letters of the words.
    
    Returns:
    A string containing the two new words separated by a space.
    """
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word2[0].upper() + new_word1[1:] + " " + new_word1[0].lower() + new_word2[1:]

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

# Welcome message and function descriptions
print("Welcome to the utility program!")
print("This program provides the following functions:")

functions = {
    "1": {
        "name": "Check for Name",
        "description": "Prompts the user for their name and checks if the name contains the letter 'a'.",
        "example_input": "John Smith",
        "expected_output": "Your name, John Smith, does not contain the letter 'a'."
    },
    "2": {
        "name": "Every Other Letter",
        "description": "Returns every other letter of a word.",
        "example_input": "Hello World",
        "expected_output": "HloWrd"
    },
    "3": {
        "name": "Reverse String",
        "description": "Reverses the characters of a word.",
        "example_input": "Hello World",
        "expected_output": "dlroW olleH"
    },
    "4": {
        "name": "Make Spoonerism",
        "description": "Prompts the user for two words and creates a Spoonerism by switching the first letters of the words.",
        "example_input": "apple banana",
        "expected_output": "Bpple anana"
    },
    "5": {
        "name": "Add Exclamation",
        "description": "Prompts the user to input strings and adds exclamation points to the end of each string until it is 20 characters long.",
        "example_input": "Hello",
        "expected_output": "Hello!!!!!!!!!!!!"
    }
}

while True:
    # Display function options
    print("\nChoose a function:")
    for key, value in functions.items():
        print(f"{key}. {value['name']} - {value['description']}")

    # Prompt user for function choice
    choice = input("Enter the function number: ")

    # Call the chosen function with user input
    if choice == "1":
        result = check_for_name()
    elif choice == "2":
        word = input("Enter a word: ")
        result = every_other_letter(word)
    elif choice == "3":
        word = input("Enter a word: ")
        result = reverse_string(word)
    elif choice == "4":
        result = make_spoonerism()
    elif choice == "5":
        result = add_exclamation()
    else:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    # Display the result and prompt for continuation
    print(f"\nResult: {result}")
    choice = input("Do you want to use another function? (y/n) ")
    if choice.lower() != "y":
        print("Thank you for using the program!")
        time.sleep(20)  # Wait 20 seconds before closing the program
        break