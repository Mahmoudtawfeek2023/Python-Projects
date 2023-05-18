def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths

# Ask the user to input the list of strings
words = []
while True:
    word = input("Enter a word (press Enter to stop): ")
    if not word:
        break
    words.append(word)

# Call the function with the user input list of strings
result_dict = word_length_dictionary(words)

# Print the resulting dictionary
print("The resulting dictionary is:", result_dict)