import string
import tkinter as tk

class StringManipulationGUI:
    def __init__(self, master):
        self.master = master
        master.title("String Manipulation Program")

        self.label = tk.Label(master, text="Welcome to the String Manipulation Program! This program provides several functions to manipulate input strings. To get started, please choose a function from the buttons below.")
        self.label.pack()

        self.unique_button = tk.Button(master, text="Count Unique English Letters", command=self.unique_english_letters)
        self.unique_button.pack()

        self.char_button = tk.Button(master, text="Count Occurrences of a Character", command=self.count_char_x)
        self.char_button.pack()

        self.substr_button = tk.Button(master, text="Count Occurrences of a Substring", command=self.count_substring)
        self.substr_button.pack()

        self.extract_button = tk.Button(master, text="Extract a Substring Between Two Characters", command=self.extract_substring)
        self.extract_button.pack()

        self.word_button = tk.Button(master, text="Check if Every Word in a Sentence Has a Length Greater Than or Equal To X", command=self.word_length)
        self.word_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def unique_english_letters(self):
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a phrase to count unique English letters:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.get_unique_letters)
        self.submit_button.pack()

    def get_unique_letters(self):
        phrase = self.entry.get()
        letters = string.ascii_letters
        unique_count = len(set(filter(lambda x: x in letters, phrase)))
        unique_letters = ", ".join(sorted(set(filter(lambda x: x in letters, phrase))))
        self.result_label = tk.Label(self.master, text=f"Number of unique English letters in '{phrase}': {unique_count}\nUnique letters: {unique_letters}")
        self.result_label.pack()

    def count_char_x(self):
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a string with no spaces:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.get_char_count)
        self.submit_button.pack()

    def get_char_count(self):
        word = self.entry.get()
        while " " in word:
            self.clear_labels()
            self.label = tk.Label(self.master, text="Invalid input. Please enter a string with no spaces:")
            self.label.pack()

            self.entry = tk.Entry(self.master)
            self.entry.pack()

            self.submit_button = tk.Button(self.master, text="Submit", command=self.get_char_count)
            self.submit_button.pack()
            return
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a character to count in the string:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=lambda: self.display_char_count(word))
        self.submit_button.pack()

    def display_char_count(self, word):
        x = self.entry.get()
        count = word.count(x)
        self.result_label = tk.Label(self.master, text=f"The character '{x}' appears {count} times in '{word}'")
        self.result_label.pack()

    def count_substring(self):
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a phrase to search for a substring:")
        self.label.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label = tk.Label(self.master, text="Enter a substring to search for in the phrase:")
        self.label.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.get_substring_count)
        self.submit_button.pack()

    def get_substring_count(self):
        phrase = self.entry1.get()
        substr = self.entry2.get()
        count = phrase.count(substr)
        self.result_label = tk.Label(self.master, text=f"The substring '{substr}' appears {count} times in '{phrase}'")
        self.result_label.pack()

    def extract_substring(self):
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a phrase to extract a substring from:")
        self.label.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label = tk.Label(self.master, text="Enter the starting character:")
        self.label.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.label = tk.Label(self.master, text="Enter the ending character:")
        self.label.pack()

        self.entry3 = tk.Entry(self.master)
        self.entry3.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.get_extracted_substring)
        self.submit_button.pack()

    def get_extracted_substring(self):
        phrase = self.entry1.get()
        start_char = self.entry2.get()
        end_char = self.entry3.get()
        start_index = phrase.find(start_char) + 1
        end_index = phrase.find(end_char)
        self.result_label = tk.Label(self.master, text=f"The substring between '{start_char}' and '{end_char}' in '{phrase}' is '{phrase[start_index:end_index]}'")
        self.result_label.pack()

    def word_length(self):
        self.clear_labels()
        self.label = tk.Label(self.master, text="Enter a sentence:")
        self.label.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label = tk.Label(self.master, text="Enter the minimum word length:")
        self.label.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_word_length)
        self.submit_button.pack()

    def check_word_length(self):
        sentence = self.entry1.get()
        min_length = int(self.entry2.get())
        words = sentence.split()
        result = all([len(word) >= min_length for word in words])
        if result:
            self.result_label = tk.Label(self.master, text=f"All words in '{sentence}' have length greater than or equal to {min_length}")
            self.result_label.pack()
        else:
            self.result_label = tk.Label(self.master, text=f"Not all words in '{sentence}' have length greater than or equal to {min_length}")
            self.result_label.pack()

    def clear_labels(self):
        for widget in self.master.pack_slaves():
            widget.destroy()

def main():
    root = tk.Tk()
    gui = StringManipulationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()