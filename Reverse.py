def reverse_string():
    """
    Reverses a string and returns the resulting string.
    Returns:
    The reversed string.
    """
    word = input("Enter a word: ")
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Call the function to test it
result = reverse_string()
print(result)