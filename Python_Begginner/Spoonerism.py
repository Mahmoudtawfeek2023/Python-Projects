def make_spoonerism():
    """
    Creates a Spoonerism by switching the first characters of two words.
    Returns:
    A string containing the two new words separated by a space.
    """
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word1 + " " + new_word2

# Call the function to create a Spoonerism
result = make_spoonerism()
# Print the result
print(result)