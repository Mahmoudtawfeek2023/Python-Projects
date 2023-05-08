def substring_between_letters(word, start, end):
    # Find the starting index of our substring using the second input parameter
    start_index = word.find(start)
    # Find the ending index of our substring using the third input parameter
    end_index = word.find(end)
    # If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
    if start_index != -1 and end_index != -1:
        return word[start_index+1:end_index]
    # If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.
    else:
        return word

# Prompt the user for input and extract substring
while True:
    word = input("Enter a string: ")
    start = input("Enter the starting character: ")
    end = input("Enter the ending character: ")
    result = substring_between_letters(word, start, end)
    print(f"The substring between '{start}' and '{end}' in '{word}' is '{result}'")
    another = input("Do you want to extract another substring? (y/n): ")
    if another.lower() != 'y':
        break