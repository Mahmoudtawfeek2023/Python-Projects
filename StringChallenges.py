import tkinter as tk
from tkinter import ttk

# Function to count the number of unique letters in a string
def unique_english_letters(word):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for letter in alphabet:
        if letter in word:
            count += 1
    return count

# Function to count the number of occurrences of a single character in a string
def count_char_x(sentence, x):
    count = 0
    for letter in sentence:
        if letter == x:
            count += 1
    return count

# Function to count the number of occurrences of a substring in a string
def count_multi_char_x(word, x):
    count = 0
    split_words = word.split(x)
    count = len(split_words) - 1
    return count

# Function to extract a substring between two characters in a string
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    if start_index != -1 and end_index != -1:
        return word[start_index+1:end_index]
    else:
        return word

# Function to check if every word in a sentence has a length greater than or equal to a specified number
def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True

# Function to display the result of the unique_english_letters() function
def display_unique_letters():
    word = entry_text.get()
    result = unique_english_letters(word)
    result_label.config(text="There are {} unique letters in the string.".format(result))

# Function to display the result of the count_char_x() function
def display_count_char_x():
    sentence = entry_text.get()
    x = char_entry.get()
    result = count_char_x(sentence, x)
    result_label.config(text="The character {} appears {} times in the sentence.".format(x, result))

# Function to display the result of the count_multi_char_x() function
def display_count_multi_char_x():
    word = entry_text.get()
    x = char_entry.get()
    result = count_multi_char_x(word, x)
    result_label.config(text="The substring {} appears {} times in the string.".format(x, result))

# Function to display the result of the substring_between_letters() function
def display_substring_between_letters():
    word = entry_text.get()
    start = start_entry.get()
    end = end_entry.get()
    result = substring_between_letters(word, start, end)
    result_label.config(text="The substring between {} and {} is {}.".format(start, end, result))

# Function to display the result of the x_length_words() function
def display_x_length_words():
    sentence = entry_text.get()
    x = int(char_entry.get())
    if x_length_words(sentence, x):
        result_label.config(text="All words in the sentence have a length of at least {} characters.".format(x))
    else:
        result_label.config(text="Not all words in the sentence have a length of at least {} characters.".format(x))

# Create the main window
root = tk.Tk()
root.title("String Manipulation Program")

# Create the notebook widget
notebook = ttk.Notebook(root)

# Create the unique letters tab
unique_letters_tab = ttk.Frame(notebook)
notebook.add(unique_letters_tab, text="Unique Letters")

# Create the unique letters widgets
unique_letters_label = ttk.Label(unique_letters_tab, text="Enter a string:")
unique_letters_label.pack(pady=10)
entry_text = tk.StringVar()
unique_letters_entry = ttk.Entry(unique_letters_tab, textvariable=entry_text)
unique_letters_entry.pack(pady=10)
unique_letters_button = ttk.Button(unique_letters_tab, text="Count Unique Letters", command=display_unique_letters)
unique_letters_button.pack(pady=10)
result_label = ttk.Label(unique_letters_tab, text="")
result_label.pack(pady=10)

# Create the count char x tab
count_char_x_tab = ttk.Frame(notebook)
notebook.add(count_char_x_tab, text="Count Char X")

# Create the count char x widgets
count_char_x_label = ttk.Label(count_char_x_tab, text="Enter a sentence:")
count_char_x_label.pack(pady=10)
entry_text = tk.StringVar()
count_char_x_entry = ttk.Entry(count_char_x_tab, textvariable=entry_text)
count_char_x_entry.pack(pady=10)
char_label = ttk.Label(count_char_x_tab, text="Enter a character:")
char_label.pack(pady=10)
char_entry = ttk.Entry(count_char_x_tab)
char_entry.pack(pady=10)
count_char_x_button = ttk.Button(count_char_x_tab, text="Count Character", command=display_count_char_x)
count_char_x_button.pack(pady=10)

# Create the count multi char x tab
count_multi_char_x_tab = ttk.Frame(notebook)
notebook.add(count_multi_char_x_tab, text="Count Multi Char X")

# Create the count multi char x widgets
count_multi_char_x_label = ttk.Label(count_multi_char_x_tab, text="Enter a string:")
count_multi_char_x_label.pack(pady=10)
entry_text = tk.StringVar()
count_multi_char_x_entry = ttk.Entry(count_multi_char_x_tab, textvariable=entry_text)
count_multi_char_x_entry.pack(pady=10)
char_label = ttk.Label(count_multi_char_x_tab, text="Enter a substring:")
char_label.pack(pady=10)
char_entry = ttk.Entry(count_multi_char_x_tab)
char_entry.pack(pady=10)
count_multi_char_x_button = ttk.Button(count_multi_char_x_tab, text="Count Substring", command=display_count_multi_char_x)
count_multi_char_x_button.pack(pady=10)

# Create the substring between letters tab
substring_between_letters_tab = ttk.Frame(notebook)
notebook.add(substring_between_letters_tab, text="Substring Between Letters")

# Create the substring between letters widgets
substring_between_letters_label = ttk.Label(substring_between_letters_tab, text="Enter a string:")
substring_between_letters_label.pack(pady=10)
entry_text = tk.StringVar()
substring_between_letters_entry = ttk.Entry(substring_between_letters_tab, textvariable=entry_text)
substring_between_letters_entry.pack(pady=10)
start_label = ttk.Label(substring_between_letters_tab, text="Enter the starting character:")
start_label.pack(pady=10)
start_entry = ttk.Entry(substring_between_letters_tab)
start_entry.pack(pady=10)
end_label = ttk.Label(substring_between_letters_tab, text="Enter the ending character:")
end_label.pack(pady=10)
end_entry = ttk.Entry(substring_between_letters_tab)
end_entry.pack(pady=10)
substring_between_letters_button = ttk.Button(substring_between_letters_tab, text="Extract Substring", command=display_substring_between_letters)
substring_between_letters_button.pack(pady=10)

# Create the x length words tab
x_length_words_tab = ttk.Frame(notebook)
notebook.add(x_length_words_tab, text="X Length Words")

# Create the x length words widgets
x_length_words_label = ttk.Label(x_length_words_tab, text="Enter a sentence:")
x_length_words_label.pack(pady=10)
entry_text = tk.StringVar()
x_length_words_entry = ttk.Entry(x_length_words_tab, textvariable=entry_text)
x_length_words_entry.pack(pady=10)
char_label = ttk.Label(x_length_words_tab, text="Enter a minimum word length:")
char_label.pack(pady=10)
char_entry = ttk.Entry(x_length_words_tab)
char_entry.pack(pady=10)
x_length_words_button = ttk.Button(x_length_words_tab, text="Check Word Length", command=display_x_length_words)
x_length_words_button.pack(pady=10)

# Pack the notebook widget
notebook.pack(fill="both", expand=True, padx=20, pady=20)

# Start the main loop
root.mainloop()