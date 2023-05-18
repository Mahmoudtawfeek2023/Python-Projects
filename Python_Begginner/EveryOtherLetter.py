def every_other_letter():
    """
    Extracts every other letter from a string and returns the resulting string.
    Returns:
    A string containing every other letter in word.
    """
    word = input("Enter a word: ")
    new_word = ""
    numberofiteration = int(input("Enter a ciphring number: "))
    for i in range(0, len(word), numberofiteration):
        new_word += word[i]
    return new_word

# Call the function to test it
result = every_other_letter()
print(result)