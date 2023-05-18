import time
import random
import string
import re
import math

# Function definitions
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

def generate_password(length):
    """
    Generates a random password of a given length.
    
    Args:
    length (int): The desired length of the password.
    
    Returns:
    A string containing a random password of the given length.
    """
    password = ""
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

def count_vowels(word):
    """
    Counts the number of vowels in a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    An integer representing the number of vowels in the input word.
    """
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

def calculate_factorial(num):
    """
    Calculates the factorial of a number.
    
    Args:
    num (int): The input number.
    
    Returns:
    An integer representing the factorial of the input number.
    """
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)

def calculate_fibonacci(num):
    """
    Calculates the nth number in the Fibonacci sequence.
    
    Args:
    num (int): The input number representing the position in the Fibonacci sequence.
    
    Returns:
    An integer representing the nth number in the Fibonacci sequence.
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return calculate_fibonacci(num - 1) + calculate_fibonacci(num - 2)

def calculate_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points in 2D space.
    
    Args:
    x1, y1, x2, y2 (float): The x and y coordinates of the two points.
    
    Returns:
    A float representing the distance between the two points.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Main program loop
while True:
    print("1. Check for the letter 'a' in a name")
    print("2. Return every other letter of a word")
    print("3. Reverse the characters of a word")
    print("4. Create a Spoonerism")
    print("5. Add exclamation points to strings")
    print("6. Generate a random password")
    print("7. Count the number of vowels in a word")
    print("8. Calculate the factorial of a number")
    print("9. Calculate the nth number in the Fibonacci sequence")
    print("10. Calculate the distance between two points in 2D space")
    print("11. Quit")
    choice = input("Enter the number of the function you want to run: ")
    if choice == "1":
        print(check_for_name())
    elif choice == "2":
        word = input("Enter a word: ")
        print(every_other_letter(word))
    elif choice == "3":
        word = input("Enter a word: ")
        print(reverse_string(word))
    elif choice == "4":
        print(make_spoonerism())
    elif choice == "5":
        print(add_exclamation())
    elif choice == "6":
        length = int(input("Enter the desired length of the password: "))
        print(generate_password(length))
    elif choice == "7":
        word = input("Enter a word: ")
        print(count_vowels(word))
    elif choice == "8":
        num = int(input("Enter a number: "))
        print(calculate_factorial(num))
    elif choice == "9":
        num = int(input("Enter a number: "))
        print(calculate_fibonacci(num))
    elif choice == "10":
        x1 = float(input("Enter the x coordinate of the first point: "))
        y1 = float(input("Enter the y coordinate of the first point: "))
        x2 = float(input("Enter the x coordinate of the second point: "))
        y2 = float(input("Enter the y coordinate of the second point: "))
        print(calculate_distance(x1, y1, x2, y2))
    elif choice == "11":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 11.")
    time.sleep(1)