def count_multi_char_x(word, x):
    # Split the input string into substrings based on the second input parameter
    substrings = word.split(x)
    # Count the number of instances the substring appeared in the first input string based on the split string
    count = len(substrings) - 1
    # Return the count of occurrences of the substring x
    return count

# Prompt the user for input and count occurrences of substring
while True:
    word = input("Enter a string: ")
    x = input("Enter a substring to search for: ")
    count = count_multi_char_x(word, x)
    print(f"The substring '{x}' appears {count} times in '{word}'")
    another = input("Do you want to search for another substring? (y/n): ")
    if another.lower() != 'y':
        break