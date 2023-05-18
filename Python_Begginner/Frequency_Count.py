def frequency_dictionary(words):
    frequency_dict = {}
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 0
        frequency_dict[word] += 1
    return frequency_dict

# Ask the user to input the list of strings
words = []
while True:
    word = input("Enter a word (press Enter to stop): ")
    if not word:
        break
    words.append(word)

# Call the function with the user input list of strings
result_dict = frequency_dictionary(words)

# Print the resulting dictionary
print("The resulting dictionary is:", result_dict)