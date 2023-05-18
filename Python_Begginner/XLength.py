def x_length_words(sentence, x):
    # Split up the sentence into an array of words
    words = sentence.split()
    # Loop through the words. If the length of any of the words is less than the provided number return False
    for word in words:
        if len(word) < x:
            return False
    # If we made it through the loop without returning False then return True
    return True

# Prompt the user for input and check if every word has a length greater than or equal to x
while True:
    sentence = input("Enter a sentence: ")
    x = int(input("Enter the minimum word length: "))
    result = x_length_words(sentence, x)
    print(f"Every word in '{sentence}' has a length greater than or equal to {x}: {result}")
    another = input("Do you want to check another sentence? (y/n): ")
    if another.lower() != 'y':
        break