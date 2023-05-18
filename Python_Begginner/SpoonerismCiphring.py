def make_spoonerism(word1, word2):
    """
    Creates a Spoonerism by switching the first letters of the first two words.
    Args:
    word1 (str): The first word.
    word2 (str): The second word.
    Returns:
    A string containing the two new words separated by a space.
    """
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word2[0].upper() + new_word1[1:] + " " + new_word1[0].lower() + new_word2[1:]

def speech_spoonerism():
    """
    Extracts the first two words after each full stop in a speech and applies the make_spoonerism function to their first letters
    Returns:
    A string containing the modified speech.
    """
    speech = input("Enter your speech: ")
    new_speech = ""
    for sentence in speech.split("."):
        words = sentence.strip().split()
        if len(words) >= 2:
            new_words = make_spoonerism(words[0], words[1])
            new_sentence = new_words + " " + " ".join(words[2:])
            new_speech += new_sentence + ". "
        else:
            new_speech += sentence.strip() + ". "
    return new_speech[:-2]

# Call the function to test it
result = speech_spoonerism()
print(result)