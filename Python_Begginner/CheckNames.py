def check_for_name():
    """
    Checks if a given name appears in a sentence. Ignores differences in capitalization.
    Returns:
    True if the name appears in the sentence (ignoring capitalization), False otherwise.
    """
    sentence = input("Enter a sentence: ")
    name = input("Enter a name: ")
    sentence_lower = sentence.lower()
    name_lower = name.lower()
    return name_lower in sentence_lower

# Call the function to test it
result = check_for_name()
print(result)