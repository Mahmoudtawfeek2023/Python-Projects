import string

def welcome_message():
    print("Welcome to the string manipulation program!")
    print("This program provides the following functions:")
    print("1. Count unique English letters")
    print("   Example input: 'Hello, World!'")
    print("   Expected output: 'Number of unique English letters in 'Hello, World!': 10\n   Unique letters: H, W, d, e, l, o, r'")
    print("2. Count occurrences of a character in a string")
    print("   Example input: 'hello', 'l'")
    print("   Expected output: 'The character 'l' appears 2 times in 'hello''")
    print("3. Count occurrences of a substring in a string")
    print("   Example input: 'hello world', 'llo'")
    print("   Expected output: 'The substring 'llo' appears 1 times in 'hello world''")
    print("4. Extract a substring between two characters")
    print("   Example input: 'abcde', 'b', 'd'")
    print("   Expected output: 'The substring between 'b' and 'd' in 'abcde' is 'c'")
    print("5. Check if every word in a sentence has a length greater than or equal to X")
    print("   Example input: 'The quick brown fox jumps over the lazy dog', 4")
    print("   Expected output: 'Every word in 'The quick brown fox jumps over the lazy dog' has a length greater than or equal to 4: True'")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number of the function you want to run: "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
            else:
                return choice
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")

def unique_english_letters():
    phrase = input("Enter a phrase to count unique English letters: ")
    letters = string.ascii_letters
    unique_count = len(set(filter(lambda x: x in letters, phrase)))
    unique_letters = ", ".join(sorted(set(filter(lambda x: x in letters, phrase))))
    print(f"Number of unique English letters in '{phrase}': {unique_count}")
    print("Unique letters:", unique_letters)

def count_char_x():
    word = input("Enter a string with no spaces: ")
    while " " in word:
        word = input("Invalid input. Please enter a string with no spaces: ")
    x = input("Enter a character to count in the string (press Enter to quit): ")
    while x != "":
        count = word.count(x)
        print(f"The character '{x}' appears {count} times in '{word}'")
        x = input("Enter another character to count in the string (press Enter to quit): ")

def count_substring():
    phrase = input("Enter a phrase to search for a substring: ")
    substr = input("Enter a substring to search for in the phrase: ")
    count = phrase.count(substr)
    print(f"The substring '{substr}' appears {count} times in '{phrase}'")

def extract_substring():
    phrase = input("Enter a phrase to extract a substring from: ")
    start_char = input("Enter the starting character: ")
    end_char = input("Enter the ending character: ")
    start_index = phrase.find(start_char) + 1
    end_index = phrase.find(end_char)
    print(f"The substring between '{start_char}' and '{end_char}' in '{phrase}' is '{phrase[start_index:end_index]}'")

def word_length():
    phrase = input("Enter a sentence to check word length: ")
    length = int(input("Enter the minimum word length: "))
    words = phrase.split()
    for word in words:
        if len(word) < length:
            print(f"'{word}' has length less than {length}")
            print(f"Every word in '{phrase}' has a length greater than or equal to {length}: False")
            return
    print(f"Every word in '{phrase}' has a length greater than or equal to {length}: True")

if __name__ == "__main__":
    welcome_message()
    choice = get_user_choice()
    if choice == 1:
        unique_english_letters()
    elif choice == 2:
        count_char_x()
    elif choice == 3:
        count_substring()
    elif choice == 4:
        extract_substring()
    else:
        word_length()